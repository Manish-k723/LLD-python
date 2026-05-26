from notification_channel import Email
from notification_service import NotificationService
from transaction import Transaction
from txn_type import TxnType


class TransactionService:
    def __init__(self):
        self._next_transaction_id = 1
        self._transactions: dict[int, Transaction] = {}
        self._notification_service = NotificationService()
        self._notification_service.add_notification_channel(Email())

    def create_txn(self, amount: float, txn_type: TxnType, source: int = None, destination: int = None):
        txn = Transaction(self._next_transaction_id, amount, source, destination, txn_type)
        self._next_transaction_id += 1
        self._transactions[txn.get_txn_id()] = txn
        return txn

    def rollback_txn(self, txn_id: int) -> None:
        txn = self._transactions.get(txn_id)
        if txn:
            txn.mark_failed()

    def mark_txn_complete(self, txn_id: int) -> None:
        txn = self._transactions.get(txn_id)
        if txn:
            txn.mark_success()

    def notify_transaction(self, txn_id: int, message: str) -> None:
        if txn_id in self._transactions:
            self._notification_service.notify(message)
