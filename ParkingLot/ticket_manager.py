from __future__ import annotations

from ParkingLot.Vehicle import Vehicle
from ParkingLot.slots import Slots
from ParkingLot.ticket import Ticket


class TicketManager:
    def __init__(self):
        self.__tickets = {}
        self.__next_ticket_number = 1

    def create_ticket(self, vehicle: Vehicle, slot: Slots):
        ticket = Ticket(self.__next_ticket_number, slot, vehicle)
        if not ticket:
            return None

        self.__tickets[self.__next_ticket_number] = ticket
        self.__next_ticket_number += 1
        return ticket

    def close_ticket(self, ticket_number: int) -> Ticket | None:
        ticket = self.__tickets.get(ticket_number)
        if not ticket:
            return None
        ticket.close()
        return ticket