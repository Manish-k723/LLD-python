from __future__ import annotations

from ParkingLot.parking_floors import ParkingFloors
from ParkingLot.parking_strategy import ParkingStrategy
from ParkingLot.slots import Slots
from typing import List

class ParkingManager:
    def __init__(self, floors: List[ParkingFloors], parking_strategy: ParkingStrategy):
        self.__floors = floors
        self.__parking_strategy = parking_strategy

    def park_vehicle(self, vehicle) -> Slots | None:
        slot = self.__parking_strategy.find_slot(self.__floors, vehicle)
        if slot is None:
            return None
        slot.park(vehicle)
        return slot
        ...
        # slot = self.__parking_strategy.find_slot(self.__floors, vehicle)
        # if slot:
        #     slot.park(vehicle)
        # return slot

    def unpark_vehicle(self, slot: Slots):
        slot.remove()