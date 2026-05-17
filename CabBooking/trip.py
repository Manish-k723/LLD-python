import dataclasses
from datetime import datetime

from CabBooking.driver import Driver
from CabBooking.location import Location
from CabBooking.trip_status import TripStatus
from rider import Rider


@dataclasses
class Trip:
    trip_id: int
    driver: Driver
    rider: Rider
    start_location: Location
    end_location: Location
    start_time: datetime
    end_time: datetime
    price: float
    trip_status: TripStatus
    otp: str

