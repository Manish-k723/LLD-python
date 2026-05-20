from vehicle_status import VehicleStatus
from vehicle_type import VehicleType


class Vehicle:
    def __init__(self, vehicle_id: int, number_plate: str, vehicle_type: VehicleType, hourly_rate: float):
        self._vehicle_id = vehicle_id
        self._number_plate = number_plate
        self._vehicle_type = vehicle_type
        self._hourly_rate = hourly_rate
        self._status = VehicleStatus.AVAILABLE

    def get_vehicle_id(self) -> int:
        return self._vehicle_id

    def get_number_plate(self) -> str:
        return self._number_plate

    def get_vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    def get_hourly_rate(self) -> float:
        return self._hourly_rate

    def get_status(self) -> VehicleStatus:
        return self._status

    def set_status(self, status: VehicleStatus) -> None:
        self._status = status
