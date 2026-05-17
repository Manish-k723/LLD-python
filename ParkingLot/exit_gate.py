from ParkingLot.Vehicle import Vehicle
from ParkingLot.gate import Gate
from ParkingLot.parking_manager import ParkingManager
from datetime import datetime
from ParkingLot.ticket_manager import TicketManager


class ExitGate(Gate):
    def __init__(self, gate_number: int, parking_manager: ParkingManager, ticket_manager: TicketManager):
        super().__init__(gate_number)
        self.__parking_manager = parking_manager
        self.__ticket_manager = ticket_manager

    def unpark_vehicle(self, car: Vehicle, ticket_number: int) -> float:
        ticket = self.__ticket_manager.close_ticket(ticket_number)
        self.__parking_manager.unpark_vehicle(ticket.get_slot())
        return self._calculate_fare(ticket.get_entry_time(), ticket.get_exit_time(), car)

    def _calculate_fare(self, entry_time: datetime, exit_time: datetime, vehicle: Vehicle) -> float:
        parked_seconds = max(1, int((exit_time - entry_time).total_seconds()))
        return float(parked_seconds * vehicle.get_vehicle_type().rate_per_second)