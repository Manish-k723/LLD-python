from __future__ import annotations

from typing import List

from ParkingLot.Vehicle import Vehicle
from ParkingLot.parking_floors import ParkingFloors
from ParkingLot.slots import Slots
from parking_strategy import ParkingStrategy

class RandomParkingStrategy(ParkingStrategy):
    def find_slot(self, parking_floor: List[ParkingFloors], vehicle: Vehicle) -> Slots | None:
        ...

