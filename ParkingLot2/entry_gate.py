from __future__ import annotations

from gate import Gate
from parking_manager import ParkingManager
from ticket import Ticket
from ticket_manager import TicketManager
from vehicle import Vehicle


class EntryGate(Gate):
    def __init__(self, gate_number: int, parking_manager: ParkingManager, ticket_manager: TicketManager):
        super().__init__(gate_number)
        self._parking_manager = parking_manager
        self._ticket_manager = ticket_manager

    def park_vehicle(self, vehicle: Vehicle) -> Ticket | None:
        slot = self._parking_manager.park_vehicle(vehicle)
        if slot is None:
            return None
        return self._ticket_manager.create_ticket(vehicle, slot)
