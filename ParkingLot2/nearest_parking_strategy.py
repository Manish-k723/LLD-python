from __future__ import annotations

from parking_floor import ParkingFloor
from parking_strategy import ParkingStrategy
from slot import Slot
from vehicle import Vehicle


class NearestParkingStrategy(ParkingStrategy):
    def find_slot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> Slot | None:
        for floor in floors:
            available_slots = floor.get_available_slots(vehicle)
            if available_slots:
                return available_slots[0]
        return None
