from __future__ import annotations

from abc import ABC, abstractmethod

from parking_floor import ParkingFloor
from slot import Slot
from vehicle import Vehicle


class ParkingStrategy(ABC):
    @abstractmethod
    def find_slot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> Slot | None:
        ...
