from CabBooking.driver_status import DriverStatus
from user import User


class Driver(User):
    def __init__(self, driver_id: int):
        self.driver_id = driver_id
        self.__status:DriverStatus = DriverStatus.AVAILABLE