from enum import Enum

class VehicleType(Enum):
    BIKE = (1, 2)
    CAR = (2, 5)
    TRUCK = (3, 10)

    def __init__(self, size: int, rate_per_second: int):
        self.size = size
        self.rate_per_second = rate_per_second