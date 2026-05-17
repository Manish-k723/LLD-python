from enum import Enum

class DriverStatus(Enum):
    AVAILABLE = 1
    ASSIGNED = 2
    ON_TRIP = 3
    OFFLINE = 4
    BLOCKED = 5