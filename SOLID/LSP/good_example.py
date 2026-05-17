class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        self.after_deposit(amount)

    def get_balance(self):
        return self._balance

    def after_deposit(self, amount):
        print(f"Deposited {amount} to account")


class WithdrawalAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount
        print(f"Withdrew {amount} from the account")


class SavingsAccount(WithdrawalAccount):
    pass


class FixedDepositAccount(BankAccount):
    pass

account = SavingsAccount()
account.deposit(100)
account.withdraw(50)

account = FixedDepositAccount(1000)
account.deposit(100)
