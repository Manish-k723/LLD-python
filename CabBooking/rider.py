from CabBooking.location import Location
from user import User


class Rider(User):
    def __init__(self, rider_id: int, name: str, phone: int, location: Location):
        super().__init__(name, phone, location)
        self.rider_id = rider_id