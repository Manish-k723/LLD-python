from datetime import datetime

from txn_status import TxnStatus
from txn_type import TxnType


class Transaction:
    def __init__(self, txn_id: int, amount: float, source: int, destination: int, txn_type: TxnType):
        self._txn_id = txn_id
        self._amount = amount
        self._source = source
        self._destination = destination
        self._timestamp: datetime = datetime.now()
        self._status: TxnStatus = TxnStatus.PENDING
        self._txn_type: TxnType = txn_type

    def mark_success(self):
        self._status = TxnStatus.SUCCESS

    def get_txn_id(self) -> int:
        return self._txn_id

    def mark_failed(self):
        self._status = TxnStatus.FAILED

    def get_amount(self) -> float:
        return self._amount

    def get_status(self) -> TxnStatus:
        return self._status

    def get_txn_type(self) -> TxnType:
        return self._txn_type

    def get_source(self) -> int:
        return self._source

    def get_destination(self) -> int:
        return self._destination

    def get_timestamp(self) -> datetime:
        return self._timestamp

    def __str__(self) -> str:
        return (f"Transaction ID: {self._txn_id}, "
                f"Amount: {self._amount}, "
                f"From: {self._source}, "
                f"To: {self._destination}, "
                f"Status: {self._status}, "
                f"Type: {self._txn_type}")
