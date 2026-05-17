from __future__ import annotations

from datetime import datetime

from ParkingLot.Vehicle import Vehicle
from ParkingLot.slots import Slots


class Ticket:
    def __init__(self, number: int, slot: Slots, vehicle: Vehicle):
        self.__number: int = number
        self.__slot: Slots = slot
        self.__vehicle: Vehicle = vehicle
        self.__entry_time: datetime = datetime.now()
        self.__exit_time: datetime | None = None

    def get_ticket_number(self) -> int:
        return self.__number
    def get_slot(self) -> Slots:
        return self.__slot
    def get_vehicle(self) -> Vehicle:
        return self.__vehicle

    def get_entry_time(self) -> datetime:
        return self.__entry_time

    def get_exit_time(self) -> datetime:
        return self.__exit_time

    def close(self) -> None:
        self.__exit_time = datetime.now()