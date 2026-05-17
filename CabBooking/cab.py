import dataclasses

from CabBooking.cab_type import CabType


class Cab:
    def __init__(self, cab_id: int, cab_type: CabType, license_plate: str):
        self.__cab_id = cab_id
        self.__cab_type = cab_type
        self.__license_plate = license_plate

    def get_cab_id(self) -> int:
        return self.__cab_id
    def get_cab_type(self) -> CabType:
        return self.__cab_type
    def get_license_plate(self) -> str:
        return self.__license_plate
