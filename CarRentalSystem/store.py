from __future__ import annotations

from vehicle import Vehicle
from vehicle_status import VehicleStatus
from vehicle_type import VehicleType


class Store:
    def __init__(self, store_id: int, city: str):
        self._store_id = store_id
        self._city = city
        self._vehicles: list[Vehicle] = []

    def get_store_id(self) -> int:
        return self._store_id

    def get_city(self) -> str:
        return self._city

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def get_available_vehicles(self, vehicle_type: VehicleType | None = None) -> list[Vehicle]:
        vehicles = [vehicle for vehicle in self._vehicles if vehicle.get_status() == VehicleStatus.AVAILABLE]
        if vehicle_type is not None:
            vehicles = [vehicle for vehicle in vehicles if vehicle.get_vehicle_type() == vehicle_type]
        return vehicles
