import time

from nearest_parking_strategy import NearestParkingStrategy
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from slot import Slot
from slot_type import SlotType
from vehicle import Vehicle
from vehicle_type import VehicleType


def build_parking_lot() -> ParkingLot:
    parking_lot = ParkingLot(NearestParkingStrategy())

    floor_1 = ParkingFloor(1)
    floor_1.add_slot(Slot(1, SlotType.SMALL))
    floor_1.add_slot(Slot(2, SlotType.MEDIUM))

    floor_2 = ParkingFloor(2)
    floor_2.add_slot(Slot(1, SlotType.MEDIUM))
    floor_2.add_slot(Slot(2, SlotType.LARGE))

    parking_lot.add_floor(floor_1)
    parking_lot.add_floor(floor_2)
    return parking_lot


parking_lot = build_parking_lot()
entry_gate = parking_lot.add_entry_gate(1)
exit_gate = parking_lot.add_exit_gate(1)

car = Vehicle("DL01AB1234", VehicleType.CAR)
ticket = entry_gate.park_vehicle(car)

if ticket is None:
    print("Parking failed")
else:
    print(f"Ticket created: {ticket.get_ticket_number()}")
    print(f"Allocated slot: {ticket.get_slot().get_slot_number()}")
    time.sleep(4)
    fare = exit_gate.exit_vehicle(ticket.get_ticket_number(), car)
    print(f"Fare: {fare}")
