from account_type import AccountType
from account import *
class AccountFactory:
    _next_account_number = 1001

    @staticmethod
    def create_account(account_type: AccountType):
        account_number = AccountFactory._next_account_number
        AccountFactory._next_account_number += 1

        if account_type == AccountType.SAVINGS:
            return SavingsAccount(account_number)
        elif account_type == AccountType.CURRENT:
            return CurrentAccount(account_number)
        raise ValueError(f"Unsupported account type: {account_type}")
