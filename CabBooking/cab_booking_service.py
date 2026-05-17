from CabBooking.driver import Driver
from CabBooking.driver_matching_service import DriverMatchingService
from CabBooking.fare_calculator import FareCalculator
from CabBooking.location import Location
from CabBooking.notification_strategy import NotificationStrategy
from CabBooking.trip_service import TripService
from CabBooking.user import User


class CabBookingService:
    def __init__(self, notification_strategy: NotificationStrategy, user: User):
        self.__user: User = user
        self.__notification_strategy = notification_strategy
        self.__driver_matching_service = DriverMatchingService()
        self.__trip_service = TripService()

    def search_cab(self, origin: Location, destination: Location):
        get_available_drivers = self.__driver_matching_service.find_nearest_available_driver(origin, destination)
        return get_available_drivers

    def book_cab(self, driver: Driver, origin: Location, destination: Location):
        self.__trip_service.book_trip(self.__user, driver, self.__notification_strategy, origin, destination)

    def cancel_trip(self):
        ...

    def complete_trip(self):
        ...

    def calculate_fare(self):
        fair_calculator = FareCalculator()
        fair_calculator.calculate_fare(self.__user.get_location().calc_distance())
