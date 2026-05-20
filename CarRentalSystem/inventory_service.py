from __future__ import annotations

from store import Store
from vehicle import Vehicle
from vehicle_type import VehicleType


class InventoryService:
    def search_vehicles(self, stores: list[Store], city: str, vehicle_type: VehicleType | None = None) -> list[Vehicle]:
        vehicles: list[Vehicle] = []
        for store in stores:
            if store.get_city().lower() != city.lower():
                continue
            vehicles.extend(store.get_available_vehicles(vehicle_type))
        return vehicles
