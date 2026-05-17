from __future__ import annotations

from typing import Any

from ParkingLot.Vehicle import Vehicle
from ParkingLot.slots import Slots
from ParkingLot2 import vehicle


class ParkingFloors:
    def __init__(self, floor_number: int, capacity: int):
        self.__floor_number = floor_number
        self.__slots = []
        self.__capacity = capacity

    def is_full(self) -> bool:
        return len(self.__slots) == self.__capacity

    def get_slot(self) -> list[Any]:
        return self.__slots

    def get_available_slots(self, vehicle: Vehicle):
        return [slot for slot in self.__slots if slot.can_fit(vehicle)]

    def add_slot(self, slot: Slots) -> str:
        if self.is_full():
            return "Floor is full"
        self.__slots.append(slot)
        return "Slot added successfully"

    def remove_slot(self, slot):
        if slot not in self.__slots:
            return "Slot not found"
        self.__slots.remove(slot)
        return "Slot removed successfully"