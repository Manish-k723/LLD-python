from __future__ import annotations

from ParkingLot.Vehicle import Vehicle
from ParkingLot.parking_floors import ParkingFloors
from ParkingLot.parking_strategy import ParkingStrategy
from ParkingLot.slots import Slots


class NearestParkingStrategy(ParkingStrategy):
    def find_slot(self, floors: list[ParkingFloors], vehicle: Vehicle) -> Slots | None:
        for floor in floors:
            available_slots = floor.get_available_slots(vehicle)
            if available_slots:
                return available_slots[0]
        return None
