from ParkingLot.slot_type import SlotType


class Slots:
    def __init__(self, slot_number: int, slot_type: SlotType):
        self.__slot_type = slot_type
        self.__slot_number = slot_number
        self.__vehicle = None

    def is_full(self) -> bool:
        return self.__vehicle is not None

    def can_fit(self, vehicle) -> bool:
        if not self.is_full():
            if self.__slot_type >= vehicle.get_vehicle_type().size:
                return True
        return False

    def park(self, vehicle) -> str:
        if self.can_fit(vehicle):
            self.__vehicle = vehicle
            return "Parked Successfully"
        return "Slot is not available"

    def remove(self) -> None:
        self.__vehicle = None
