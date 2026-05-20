from datetime import datetime

from inventory_service import InventoryService
from reservation import Reservation
from reservation_service import ReservationService
from store import Store
from user import User
from vehicle import Vehicle
from vehicle_type import VehicleType


class CarRentalSystem:
    def __init__(self):
        self._stores: list[Store] = []
        self._inventory_service = InventoryService()
        self._reservation_service = ReservationService()

    def add_store(self, store: Store) -> None:
        self._stores.append(store)

    def search(self, city: str, vehicle_type: VehicleType | None = None) -> list[Vehicle]:
        return self._inventory_service.search_vehicles(self._stores, city, vehicle_type)

    def reserve_vehicle(
        self, user: User, vehicle: Vehicle, start_time: datetime, end_time: datetime
    ) -> Reservation | None:
        return self._reservation_service.create_reservation(user, vehicle, start_time, end_time)

    def complete_reservation(self, reservation_id: int):
        return self._reservation_service.complete_reservation(reservation_id)
