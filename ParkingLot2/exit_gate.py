from __future__ import annotations

from datetime import datetime

from vehicle import Vehicle
from gate import Gate
from parking_manager import ParkingManager
from ticket_manager import TicketManager


class ExitGate(Gate):
    def __init__(self, gate_number: int, parking_manager: ParkingManager, ticket_manager: TicketManager):
        super().__init__(gate_number)
        self._parking_manager = parking_manager
        self._ticket_manager = ticket_manager

    def exit_vehicle(self, ticket_number: int, vehicle: Vehicle) -> float | None:
        ticket = self._ticket_manager.close_ticket(ticket_number)
        if ticket is None:
            return None

        self._parking_manager.unpark_vehicle(ticket.get_slot())
        return self._calculate_fare(ticket.get_entry_time(), ticket.get_exit_time(), vehicle)

    def _calculate_fare(self, entry_time: datetime, exit_time: datetime, vehicle: Vehicle) -> float:
        parked_seconds = max(1, int((exit_time - entry_time).total_seconds()))
        return float(parked_seconds * vehicle.get_vehicle_type().rate_per_second)
