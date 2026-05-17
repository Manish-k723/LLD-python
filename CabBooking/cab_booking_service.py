from __future__ import annotations

from CabBooking.cab_type import CabType
from CabBooking.driver import Driver
from CabBooking.driver_availability_service import DriverAvailabilityService
from CabBooking.driver_matching_service import DriverMatchingService
from CabBooking.fare_calculator import FareCalculator
from CabBooking.location import Location
from CabBooking.notification_strategy import NotificationStrategy
from CabBooking.payment_service import PaymentService
from CabBooking.trip_service import TripService
from CabBooking.rider import Rider
from typing import List


class CabBookingService:
    def __init__(self, riders: List[Rider], drivers: List[Driver], notification_strategy: NotificationStrategy, payment_service: PaymentService):
        self.__riders = {rider.get_rider_id(): rider for rider in riders}
        self.__notification_strategy = notification_strategy
        self.__payment_service = payment_service
        self.__driver_availability_service = DriverAvailabilityService(drivers)
        self.__driver_matching_service = DriverMatchingService(self.__driver_availability_service)
        self.__trip_service = TripService(notification_strategy, FareCalculator(), self.__driver_availability_service)

    def search_cab(self, origin: Location, cab_type: CabType | None = None):
        return self.__driver_matching_service.get_nearest_drivers(origin, cab_type)

    def book_cab(self, rider_id: int, origin: Location, cab_type: CabType | None = None, drop: Location | None = None):
        rider = self.__riders.get(rider_id)
        if rider is None:
            return None

        driver = self.__driver_matching_service.get_matching_driver(origin, cab_type)
        if driver is None:
            return None

        rider.update_location(origin)
        driver.update_location(origin)
        return self.__trip_service.create_trip(rider, driver, origin, drop)

    def cancel_trip(self):
        ...

    def complete_trip(self, trip_id: int):
        trip = self.__trip_service.complete_trip(trip_id)
        if trip is None:
            return None
        self.__payment_service.pay(trip.get_estimated_fare())
        return trip

    def start_trip(self, trip_id: int):
        self.__trip_service.start_trip(trip_id)
