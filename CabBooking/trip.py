from __future__ import annotations

import dataclasses
from datetime import datetime

from CabBooking.driver import Driver
from CabBooking.location import Location
from CabBooking.trip_status import TripStatus
from rider import Rider


class Trip:
    def __init__(self, trip_id: int, driver: Driver, rider: Rider, origin: Location, destination: Location, fare: float):
        self.__next_trip_id = trip_id
        self.__rider = rider
        self.__driver = driver
        self.__pickup: Location = origin
        self.__drop: Location = destination
        self.__start_time = datetime.now()
        self.__end_time: datetime | None = None
        self.__status = TripStatus.DRIVER_ASSIGNED
        self.__created_at = datetime.now()
        self.__estimated_fare: float = fare

    def get_trip_id(self) -> int:
        return self.__next_trip_id
    def get_rider(self) -> Rider:
        return self.__rider
    def get_driver(self) -> Driver:
        return self.__driver
    def get_pickup(self) -> Location:
        return self.__pickup
    def get_drop_location(self) -> Location:
        return self.__drop
    def get_start_time(self) -> datetime:
        return self.__start_time
    def get_estimated_fare(self):
        return self.__estimated_fare
    def start(self) -> None:
        self.__status = TripStatus.STARTED

    def complete(self) -> None:
        self.__status = TripStatus.ENDED


