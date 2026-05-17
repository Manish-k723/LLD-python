from __future__ import annotations

from ticket import Ticket
from slot import Slot
from vehicle import Vehicle


class TicketManager:
    def __init__(self):
        self._tickets: dict[int, Ticket] = {}
        self._next_ticket_number = 1

    def create_ticket(self, vehicle: Vehicle, slot: Slot) -> Ticket:
        ticket = Ticket(self._next_ticket_number, vehicle, slot)
        self._tickets[ticket.get_ticket_number()] = ticket
        self._next_ticket_number += 1
        return ticket

    def get_ticket(self, ticket_number: int) -> Ticket | None:
        return self._tickets.get(ticket_number)

    def close_ticket(self, ticket_number: int) -> Ticket | None:
        ticket = self._tickets.get(ticket_number)
        if ticket is None:
            return None
        ticket.close()
        return ticket
