from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ParkingLot.Vehicle import Vehicle
from ParkingLot.parking_floors import ParkingFloors
from ParkingLot.slots import Slots


class ParkingStrategy(ABC):
    @abstractmethod
    def find_slot(self, parking_floor: List[ParkingFloors], vehicle: Vehicle) -> Slots | None:
        ...