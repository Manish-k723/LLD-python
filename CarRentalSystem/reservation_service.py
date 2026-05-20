from datetime import datetime

from billing_service import BillingService
from payment_service import PaymentService
from reservation import Reservation
from user import User
from vehicle import Vehicle
from vehicle_status import VehicleStatus


class ReservationService:
    def __init__(self):
        self._next_reservation_id = 1
        self._reservations: dict[int, Reservation] = {}
        self._billing_service = BillingService()
        self._payment_service = PaymentService()

    def create_reservation(
        self, user: User, vehicle: Vehicle, start_time: datetime, end_time: datetime
    ) -> Reservation | None:
        if vehicle.get_status() != VehicleStatus.AVAILABLE:
            return None

        reservation = Reservation(self._next_reservation_id, user, vehicle, start_time, end_time)
        reservation.activate()
        vehicle.set_status(VehicleStatus.RESERVED)
        self._reservations[reservation.get_reservation_id()] = reservation
        self._next_reservation_id += 1
        return reservation

    def complete_reservation(self, reservation_id: int):
        reservation = self._reservations.get(reservation_id)
        if reservation is None:
            return None, None

        reservation.complete()
        reservation.get_vehicle().set_status(VehicleStatus.AVAILABLE)
        amount = self._billing_service.calculate_amount(reservation)
        payment = self._payment_service.pay(amount)
        return reservation, payment

    def cancel_reservation(self, reservation_id: int) -> Reservation | None:
        reservation = self._reservations.get(reservation_id)
        if reservation is None:
            return None
        reservation.cancel()
        reservation.get_vehicle().set_status(VehicleStatus.AVAILABLE)
        return reservation
