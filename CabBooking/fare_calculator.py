from CabBooking.location import Location
from CabBooking.cab_type import CabType

class FareCalculator:
    def calculate_fare(self, pickup: Location, drop: Location, cab_type: CabType) -> float:
        distance = pickup.distance_to(drop)
        return distance * cab_type.rate_per_distance