from __future__ import annotations

from user import User
from account import Account
from account_status import AccountStatus
from transaction_service import TransactionService
from txn_type import TxnType

class Bank:
    def __init__(self, bank_id: int = 1, name: str = "Bank"):
        self._bank_id: int = bank_id
        self._name: str = name
        self.users: dict[int, User] = {}
        self._accounts: dict[int, Account] = {}
        self._transaction_service = TransactionService()

    def add_user(self, user: User):
        self.users[user.get_id()] = user
        for account in user.get_accounts():
            self.add_account(account)

    def remove_user(self, user_id: int):
        self.users.pop(user_id)

    def get_user(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def add_account(self, account: Account):
        self._accounts[account.get_account_number()] = account

    def deposit(self, account_number: int, amount: float):
        account = self._accounts.get(account_number)
        if account is None:
            raise ValueError(f"Account {account_number} does not exist")
        if not account.validate_transaction(TxnType.DEPOSIT, amount):
            raise ValueError(f"Deposit of {amount} is not allowed for account {account_number}")

        txn = self._transaction_service.create_txn(
            amount=amount,
            txn_type=TxnType.DEPOSIT,
            destination=account_number,
        )

        account.deposit(amount)
        account.add_transaction(txn)
        self._transaction_service.mark_txn_complete(txn.get_txn_id())
        self._transaction_service.notify_transaction(
            txn.get_txn_id(),
            f"Deposit of {amount} completed for account {account_number}",
        )
        return txn

    def withdraw(self, account_number: int, amount: float):
        account = self._accounts.get(account_number)
        if account is None:
            raise ValueError(f"Account {account_number} does not exist")
        if not account.validate_transaction(TxnType.WITHDRAWAL, amount):
            raise ValueError(f"Withdrawal of {amount} is not allowed for account {account_number}")

        txn = self._transaction_service.create_txn(
            amount=amount,
            txn_type=TxnType.WITHDRAWAL,
            source=account_number,
        )
        account.withdraw(amount)
        account.add_transaction(txn)
        self._transaction_service.mark_txn_complete(txn.get_txn_id())
        self._transaction_service.notify_transaction(
            txn.get_txn_id(),
            f"Withdrawal of {amount} completed for account {account_number}",
        )
        return txn

    def transfer(self, source_account_number: int, destination_account_number: int, amount: float):
        source_account = self._accounts.get(source_account_number)
        destination_account = self._accounts.get(destination_account_number)

        if source_account is None:
            raise ValueError(f"Source account {source_account_number} does not exist")
        if destination_account is None:
            raise ValueError(f"Destination account {destination_account_number} does not exist")
        if source_account_number == destination_account_number:
            raise ValueError("Source and destination accounts should be different")
        if source_account.get_account_status() != AccountStatus.ACTIVE:
            raise ValueError(f"Source account {source_account_number} is not active")
        if destination_account.get_account_status() != AccountStatus.ACTIVE:
            raise ValueError(f"Destination account {destination_account_number} is not active")
        if not source_account.validate_transaction(TxnType.WITHDRAWAL, amount):
            raise ValueError(f"Transfer of {amount} is not allowed for account {source_account_number}")

        txn = self._transaction_service.create_txn(
            amount=amount,
            txn_type=TxnType.TRANSFER,
            source=source_account_number,
            destination=destination_account_number,
        )

        try:
            source_account.withdraw(amount)
            destination_account.deposit(amount)
            source_account.add_transaction(txn)
            destination_account.add_transaction(txn)
            self._transaction_service.mark_txn_complete(txn.get_txn_id())
            self._transaction_service.notify_transaction(
                txn.get_txn_id(),
                (
                    f"Transfer of {amount} completed from account "
                    f"{source_account_number} to {destination_account_number}"
                ),
            )
            return txn
        except Exception:
            destination_account.withdraw(amount)
            source_account.deposit(amount)
            self._transaction_service.rollback_txn(txn.get_txn_id())
            raise
