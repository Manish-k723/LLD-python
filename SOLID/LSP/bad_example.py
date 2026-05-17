from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance=0):
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} to savings account")

    @abstractmethod
    def withdraw(self, amount):
        ...

class SavingsAccount(BankAccount):
    def __init__(self, balance: int = 0):
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount) -> None:
        if self.__balance < amount:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} from savings account")

class FixedDepositAccount(BankAccount):
    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        raise Exception("Cannot withdraw from fixed deposit account")

account = SavingsAccount()
account.deposit(100)
account.withdraw(50)

account = FixedDepositAccount()
account.deposit(100)
account.withdraw(50)
