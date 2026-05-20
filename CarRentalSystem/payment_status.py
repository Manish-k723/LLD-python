from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    PAID = 2
    FAILED = 3
