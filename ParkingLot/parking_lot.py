from typing import List

from ParkingLot.entry_gate import EntryGate
from ParkingLot.exit_gate import ExitGate
from ParkingLot.parking_floors import ParkingFloors
from ParkingLot.parking_strategy import ParkingStrategy
from ParkingLot.parking_manager import ParkingManager
from ParkingLot.ticket_manager import TicketManager


class ParkingLot:
    def __init__(self, parking_strategy: ParkingStrategy):
        self.__parking_floors: List[ParkingFloors] = []
        self.__entry_gates = []
        self.__exit_gates = []
        self.__parking_manager = ParkingManager(self.__parking_floors, parking_strategy)
        self.__ticket_manager = TicketManager()

    def add_floor(self, floor: ParkingFloors):
        self.__parking_floors.append(floor)

    def add_entry_gate(self, gate_number: int) -> EntryGate:
        entry_gate = EntryGate(gate_number, self.__parking_manager, self.__ticket_manager)
        self.__entry_gates.append(entry_gate)
        return entry_gate

    def add_exit_gate(self, gate_number: int) -> ExitGate:
        exit_gate = ExitGate(gate_number, self.__parking_manager, self.__ticket_manager)
        self.__exit_gates.append(exit_gate)
        return exit_gate



