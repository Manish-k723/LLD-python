from datetime import datetime

from account import *


class StatementService:
    def generate_statement(self, account: Account, start: datetime, end: datetime) -> list:
        statement = []
        txns = account.get_user_transactions()
        for txn in txns:
            if start <= txn.get_timestamp() <= end:
                statement.append(txn)
        return statement

