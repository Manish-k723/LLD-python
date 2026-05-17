from CabBooking.driver import Driver
from CabBooking.driver_status import DriverStatus


class DriverAvailabilityService:
    def __init__(self, drivers: list[Driver]):
        self._drivers = drivers

    def get_available_drivers(self):
        return [driver for driver in self._drivers if driver.is_available()]

    def book_driver(self):
        ...
    def cancel_trip(self):
        ...
    def mark_available(self, driver: Driver):
        driver.set_status(DriverStatus.AVAILABLE)

    def mark_on_trip(self, driver: Driver):
        driver.set_status(DriverStatus.ON_TRIP)