from __future__ import annotations

from account_factory import AccountFactory
from account_type import AccountType
from account import *
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name
        self._email = email
        self._accounts: dict[int, Account] = {}

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def update_details(self, name: str | None = None, email: str | None = None):
        if name is not None:
            self._name = name
        if email is not None:
            self._email = email

    def add_account(self, account_type: AccountType, balance: float = 0.0) -> Account:
        user_new_account = AccountFactory.create_account(account_type)
        self._accounts[user_new_account.get_account_number()] = user_new_account
        user_new_account.deposit(balance)
        return user_new_account

    def get_accounts(self) -> list[Account]:
        return list(self._accounts.values())
