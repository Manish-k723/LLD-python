from __future__ import annotations

from datetime import datetime

from slot import Slot
from vehicle import Vehicle


class Ticket:
    def __init__(self, ticket_number: int, vehicle: Vehicle, slot: Slot):
        self._ticket_number = ticket_number
        self._vehicle = vehicle
        self._slot = slot
        self._entry_time = datetime.now()
        self._exit_time: datetime | None = None

    def get_ticket_number(self) -> int:
        return self._ticket_number

    def get_vehicle(self) -> Vehicle:
        return self._vehicle

    def get_slot(self) -> Slot:
        return self._slot

    def get_entry_time(self) -> datetime:
        return self._entry_time

    def get_exit_time(self) -> datetime | None:
        return self._exit_time

    def close(self) -> None:
        self._exit_time = datetime.now()
