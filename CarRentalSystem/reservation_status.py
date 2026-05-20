from enum import Enum


class ReservationStatus(Enum):
    CREATED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELLED = 4
