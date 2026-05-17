import random

from parking_floor import ParkingFloor
from parking_strategy import ParkingStrategy
from slot import Slot
from vehicle import Vehicle


class RandomParkingStrategy(ParkingStrategy):
    def find_slot(self, floors: list[ParkingFloor], vehicle: Vehicle) -> Slot | None:
        candidates: list[Slot] = []
        for floor in floors:
            candidates.extend(floor.get_available_slots(vehicle))

        if not candidates:
            return None
        return random.choice(candidates)
