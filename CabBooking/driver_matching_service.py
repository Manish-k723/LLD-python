from CabBooking.driver_availability_service import DriverAvailabilityService
from CabBooking.location import Location


class DriverMatchingService:
    def __init__(self):
        self.__driver_availability_service = DriverAvailabilityService()

    def find_nearest_available_driver(self, origin: Location, destination: Location):
        pass

    def get_best_driver(self):
        pass
