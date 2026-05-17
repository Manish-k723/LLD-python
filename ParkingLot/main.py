from ParkingLot.Vehicle import Vehicle
from ParkingLot.parking_lot import ParkingLot
from ParkingLot.slot_type import SlotType
from ParkingLot.vehicle_type import VehicleType
from nearest_parking_strategy import NearestParkingStrategy
from parking_floors import ParkingFloors
from slots import Slots
import time

parking_lot = ParkingLot(NearestParkingStrategy())

floor1 = ParkingFloors(1, 10)
floor1.add_slot(Slots(1, SlotType.SMALL))
floor1.add_slot(Slots(2, SlotType.LARGE))
parking_lot.add_floor(floor1)

floor2 = ParkingFloors(2, 10)
floor2.add_slot(Slots(1, SlotType.MEDIUM))
floor2.add_slot(Slots(2, SlotType.LARGE))
parking_lot.add_floor(floor2)

entry_gate = parking_lot.add_entry_gate(1)
exit_gate = parking_lot.add_exit_gate(1)

car = Vehicle("DL01AB1234", VehicleType.CAR)
ticket = entry_gate.park_vehicle(car)

if ticket:
    print(f"Parking successful with {ticket.get_ticket_number()}")
    time.sleep(1)
    fare = exit_gate.unpark_vehicle(car, ticket.get_ticket_number())
    print(f"Your Total Fare is: {fare}")
else:
    print("Parking failed")

truck = Vehicle("Penka Ka Truck", VehicleType.TRUCK)
ticket = entry_gate.park_vehicle(truck)
if ticket:
    print(f"Parking successful with {ticket.get_ticket_number()}")
    time.sleep(3)
    fare = exit_gate.unpark_vehicle(truck, ticket.get_ticket_number())
    print(f"Your Total Fare is: {fare}, Please pay the amount {truck.get_license_plate()}")









