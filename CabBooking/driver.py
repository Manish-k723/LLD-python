from CabBooking.cab import Cab
from CabBooking.driver_status import DriverStatus
from CabBooking.location import Location
from user import User


class Driver(User):
    def __init__(self, driver_id: int, name: str, phone: str, location: Location, cab: Cab):
        super().__init__(name, phone, location)
        self.driver_id = driver_id
        self.__status:DriverStatus = DriverStatus.AVAILABLE
        self.__cab:Cab = cab

    def get_cab(self) -> Cab:
        return self.__cab

    def get_status(self) -> DriverStatus:
        return self.__status

    def set_status(self, status: DriverStatus) -> None:
        self.__status = status

    def is_available(self) -> bool:
        return self.__status == DriverStatus.AVAILABLE