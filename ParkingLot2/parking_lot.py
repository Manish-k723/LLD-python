from entry_gate import EntryGate
from exit_gate import ExitGate
from parking_floor import ParkingFloor
from parking_manager import ParkingManager
from parking_strategy import ParkingStrategy
from ticket_manager import TicketManager


class ParkingLot:
    def __init__(self, parking_strategy: ParkingStrategy):
        self._floors: list[ParkingFloor] = []
        self._ticket_manager = TicketManager()
        self._parking_manager = ParkingManager(self._floors, parking_strategy)
        self._entry_gates: list[EntryGate] = []
        self._exit_gates: list[ExitGate] = []

    def add_floor(self, floor: ParkingFloor) -> None:
        self._floors.append(floor)

    def add_entry_gate(self, gate_number: int) -> EntryGate:
        gate = EntryGate(gate_number, self._parking_manager, self._ticket_manager)
        self._entry_gates.append(gate)
        return gate

    def add_exit_gate(self, gate_number: int) -> ExitGate:
        gate = ExitGate(gate_number, self._parking_manager, self._ticket_manager)
        self._exit_gates.append(gate)
        return gate

    def get_floors(self) -> list[ParkingFloor]:
        return self._floors
