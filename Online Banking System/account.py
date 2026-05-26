from typing import List

from account_status import AccountStatus
from transaction import Transaction
from txn_type import TxnType


class Account:
    def __init__(self, account_number: int = 0, account_status: AccountStatus = AccountStatus.ACTIVE, balance: float = 0):
        self._account_number = account_number
        self._account_status = account_status
        self._balance = balance
        self._transactions: dict[int, Transaction] = {}

    def get_account_number(self) -> int:
        return self._account_number

    def get_account_status(self) -> AccountStatus:
        return self._account_status

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions[transaction.get_txn_id()] = transaction

    def validate_transaction(self, txn_type: TxnType, amount: float) -> bool:
        if amount <= 0:
            return False
        if self._account_status != AccountStatus.ACTIVE:
            return False
        if txn_type == TxnType.DEPOSIT:
            return True
        if txn_type == TxnType.WITHDRAWAL:
            return self.can_withdraw(amount)
        return False

    def can_withdraw(self, amount: float) -> bool:
        return self._balance - amount >= 0

    def get_user_transactions(self) -> List[Transaction]:
        return list(self._transactions.values())


class SavingsAccount(Account):
    @staticmethod
    def minimum_balance_requirement() -> float:
        return 500

    def can_withdraw(self, amount: float) -> bool:
        return self.get_balance() - amount >= self.minimum_balance_requirement()


class CurrentAccount(Account):
    @staticmethod
    def available_overdraft() -> float:
        return 5000

    def can_withdraw(self, amount: float) -> bool:
        return self.get_balance() + self.available_overdraft() - amount >= 0
