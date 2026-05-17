from __future__ import annotations

from CabBooking.cab_type import CabType
from CabBooking.driver import Driver
from CabBooking.driver_availability_service import DriverAvailabilityService
from CabBooking.location import Location


class DriverMatchingService:
    def __init__(self, driver_availability_service: DriverAvailabilityService):
        self.__driver_availability_service = driver_availability_service

    def get_nearest_drivers(self, origin: Location, cab_type: CabType | None = None):
        candidates = self.__driver_availability_service.get_available_drivers()

        if cab_type is not None:
            candidates = [candidate for candidate in candidates if candidate.get_cab().get_cab_type() == cab_type]

        return sorted(candidates, key=lambda driver: driver.get_location().distance_to(origin))

    def get_matching_driver(self, origin: Location, cab_type: CabType | None = None) -> Driver | None:
        candidate = self.get_nearest_drivers(origin, cab_type)[0]
        return candidate if candidate else None
