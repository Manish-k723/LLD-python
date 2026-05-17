from vehicle_type import VehicleType


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self._license_plate = license_plate
        self._vehicle_type = vehicle_type

    def get_license_plate(self) -> str:
        return self._license_plate

    def get_vehicle_type(self) -> VehicleType:
        return self._vehicle_type
