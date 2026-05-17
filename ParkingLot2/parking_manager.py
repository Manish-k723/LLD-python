from __future__ import annotations

from parking_floor import ParkingFloor
from parking_strategy import ParkingStrategy
from slot import Slot
from vehicle import Vehicle


class ParkingManager:
    def __init__(self, floors: list[ParkingFloor], parking_strategy: ParkingStrategy):
        self._floors = floors
        self._parking_strategy = parking_strategy

    def park_vehicle(self, vehicle: Vehicle) -> Slot | None:
        slot = self._parking_strategy.find_slot(self._floors, vehicle)
        if slot is None:
            return None

        parked = slot.park(vehicle)
        if not parked:
            return None
        return slot

    def unpark_vehicle(self, slot: Slot) -> Vehicle | None:
        return slot.unpark()
