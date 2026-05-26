from enum import Enum

class TxnStatus(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"