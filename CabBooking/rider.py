from CabBooking.location import Location
from user import User


class Rider(User):
    def __init__(self, rider_id: int, name: str, phone: str, location: Location):
        super().__init__(name, phone, location)
        self.rider_id = rider_id

    def get_rider_id(self) -> int:
        return self.rider_id