from enum import Enum

class TripStatus(Enum):
    REQUESTED = 1
    DRIVER_ASSIGNED = 2
    DRIVER_ARRIVED = 3
    STARTED = 4
    ENDED = 5
    CANCELLED = 6
    PAYMENT_PENDING = 7
    PAYMENT_COMPLETED = 8
