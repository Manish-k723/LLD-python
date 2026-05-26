from datetime import datetime, timedelta

from user import User
from bank import Bank
from account_type import AccountType
from statement_service import StatementService

user1 = User(1, "Manish", "gmail.com")
user2 = User(2, "Priyanka", "yahoo.com")

user1_account = user1.add_account(AccountType.SAVINGS, 100000)
user2_account = user2.add_account(AccountType.SAVINGS, 10)

kotak_bank = Bank(name="Kotak Bank")

kotak_bank.add_user(user1)
kotak_bank.add_user(user2)
kotak_bank.deposit(user1_account.get_account_number(), 10000)
kotak_bank.withdraw(user1_account.get_account_number(), 10000)
kotak_bank.transfer(user1_account.get_account_number(), user2_account.get_account_number(), 2000)

print(user1_account.get_balance())
print(user2_account.get_balance())

statement_service = StatementService()
statement = statement_service.generate_statement(
    user1_account,
    datetime.now() - timedelta(days=1),
    datetime.now() + timedelta(days=1),
)
for txn in statement:
    print(txn)
