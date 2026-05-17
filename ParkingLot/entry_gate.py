from ParkingLot.Vehicle import Vehicle
from ParkingLot.gate import Gate
from ParkingLot.parking_manager import ParkingManager
from ParkingLot.ticket_manager import TicketManager


class EntryGate(Gate):
    def __init__(self, number, parking_manager: ParkingManager, ticket_manager: TicketManager):
        super().__init__(number)
        self.__parking_manager = parking_manager
        self.__ticket_manager = ticket_manager

    def park_vehicle(self, vehicle: Vehicle):
        slot = self.__parking_manager.park_vehicle(vehicle)
        if slot is None:
            return None
        return self.__ticket_manager.create_ticket(vehicle, slot)