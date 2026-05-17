from enum import Enum

class CabType(Enum):
    HATCHBACK = ("Hatchback", 10)
    SEDAN = ("Sedan", 12)
    SUV = ("SUV", 15)

    def __init__(self, display_name: str, rate_per_distance: int):
        self.display_name = display_name
        self.rate_per_distance = rate_per_distance