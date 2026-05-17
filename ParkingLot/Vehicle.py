from vehicle_type import VehicleType


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.__license_plate = license_plate
        self.__vehicle_type = vehicle_type

    def get_license_plate(self) -> str:
        return self.__license_plate
    def get_vehicle_type(self) -> VehicleType:
        return self.__vehicle_type

    def get_price(self) -> float:
        return self.__vehicle_type.rate_per_second
