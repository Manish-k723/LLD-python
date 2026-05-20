from datetime import datetime, timedelta

from car_rental_system import CarRentalSystem
from store import Store
from user import User
from vehicle import Vehicle
from vehicle_type import VehicleType


system = CarRentalSystem()

delhi_store = Store(1, "Delhi")
delhi_store.add_vehicle(Vehicle(1, "DL1AB1234", VehicleType.HATCHBACK, 100))
delhi_store.add_vehicle(Vehicle(2, "DL1AB5678", VehicleType.SEDAN, 150))
delhi_store.add_vehicle(Vehicle(3, "DL1AB9999", VehicleType.SUV, 200))
system.add_store(delhi_store)

user = User(1, "Manish", "DL-042024-1234567")
available_cars = system.search("Delhi", VehicleType.SEDAN)

print("Available cars:")
for car in available_cars:
    print(car.get_vehicle_id(), car.get_number_plate(), car.get_vehicle_type().name)

start_time = datetime.now()
end_time = start_time + timedelta(hours=5)
reservation = system.reserve_vehicle(user, available_cars[0], start_time, end_time)

if reservation is not None:
    print(f"Reservation created: {reservation.get_reservation_id()}")
    completed_reservation, payment = system.complete_reservation(reservation.get_reservation_id())
    print(f"Reservation status: {completed_reservation.get_status().name}")
    print(f"Payment amount: {payment.get_amount()}")
