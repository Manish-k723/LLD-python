from __future__ import annotations

from datetime import datetime

from CabBooking.cab_type import CabType
from CabBooking.driver_availability_service import DriverAvailabilityService
from CabBooking.fare_calculator import FareCalculator
from CabBooking.location import Location
from CabBooking.notification_service import NotificationService
from CabBooking.trip import Trip
from CabBooking2.notification_strategy import NotificationStrategy


class TripService:
    def __init__(self, notification_strategy: NotificationStrategy, fare_calculator: FareCalculator, driver_availability_service: DriverAvailabilityService):
        self.__trips = {}
        self._driver_availability_service = driver_availability_service
        self.__notification_service = NotificationService(notification_strategy)
        self.__fare_calculator = fare_calculator
        self.__next_trip_id = 1

    def get_trip(self) -> Trip:
        return self.__trip

    def create_trip(self, user, driver, origin: Location, destination: Location):
        fare = self.__fare_calculator.calculate_fare(origin, destination, driver.get_cab().get_cab_type())
        trip = Trip(self.__next_trip_id, driver, user, origin, destination, fare)
        self.__trips[trip.get_trip_id()] = trip
        self._driver_availability_service.mark_on_trip(driver)
        self.__notification_service.notify_rider(
            f"Trip booked with {driver.get_name()} for you with Fare of {fare}"
        )
        self.__notification_service.notify_driver(
            f"Rider {user.get_name()} booked a trip with you at {datetime.now()} at {origin}"
        )
        self.__next_trip_id += 1
        return trip

    def end_trip(self):
        pass

    def cancel_trip(self):
        pass

    def start_trip(self, trip_id: int):
        trip = self.__trips.get(trip_id)
        if trip is None:
            return None
        self.__notification_service.notify_driver(
            f"Trip {trip_id} started at {datetime.now()}"
        )
        self.__notification_service.notify_rider(
            f"Trip {trip_id} started at {datetime.now()}"
        )
        trip.start()
        return trip

    def complete_trip(self, trip_id: int):
        trip = self.__trips.get(trip_id)
        if trip is None:
            return None
        self.__notification_service.notify_driver(
            f"Trip {trip_id} completed at {datetime.now()}"
        )
        self.__notification_service.notify_rider(
            f"Trip {trip_id} completed at {datetime.now()}"
        )
        trip.complete()
        self._driver_availability_service.mark_available(trip.get_driver())
        trip.get_driver().update_location(trip.get_drop_location())
        trip.get_rider().update_location(trip.get_drop_location())
        return trip
