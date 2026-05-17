from __future__ import annotations

from slot import Slot
from vehicle import Vehicle


class ParkingFloor:
    def __init__(self, floor_number: int):
        self._floor_number = floor_number
        self._slots: list[Slot] = []

    def get_floor_number(self) -> int:
        return self._floor_number

    def add_slot(self, slot: Slot) -> None:
        self._slots.append(slot)

    def get_slots(self) -> list[Slot]:
        return self._slots

    def get_available_slots(self, vehicle: Vehicle) -> list[Slot]:
        return [slot for slot in self._slots if slot.can_fit(vehicle)]
