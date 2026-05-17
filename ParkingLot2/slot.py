from __future__ import annotations

from slot_type import SlotType
from vehicle import Vehicle


class Slot:
    def __init__(self, slot_number: int, slot_type: SlotType):
        self._slot_number = slot_number
        self._slot_type = slot_type
        self._parked_vehicle: Vehicle | None = None

    def get_slot_number(self) -> int:
        return self._slot_number

    def get_slot_type(self) -> SlotType:
        return self._slot_type

    def is_free(self) -> bool:
        return self._parked_vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.is_free() and self._slot_type >= vehicle.get_vehicle_type().size

    def park(self, vehicle: Vehicle) -> bool:
        if not self.can_fit(vehicle):
            return False
        self._parked_vehicle = vehicle
        return True

    def unpark(self) -> Vehicle | None:
        vehicle = self._parked_vehicle
        self._parked_vehicle = None
        return vehicle
