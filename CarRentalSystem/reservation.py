from datetime import datetime

from reservation_status import ReservationStatus
from user import User
from vehicle import Vehicle


class Reservation:
    def __init__(self, reservation_id: int, user: User, vehicle: Vehicle, start_time: datetime, end_time: datetime):
        self._reservation_id = reservation_id
        self._user = user
        self._vehicle = vehicle
        self._start_time = start_time
        self._end_time = end_time
        self._status = ReservationStatus.CREATED

    def get_reservation_id(self) -> int:
        return self._reservation_id

    def get_user(self) -> User:
        return self._user

    def get_vehicle(self) -> Vehicle:
        return self._vehicle

    def get_start_time(self) -> datetime:
        return self._start_time

    def get_end_time(self) -> datetime:
        return self._end_time

    def get_status(self) -> ReservationStatus:
        return self._status

    def activate(self) -> None:
        self._status = ReservationStatus.ACTIVE

    def complete(self) -> None:
        self._status = ReservationStatus.COMPLETED

    def cancel(self) -> None:
        self._status = ReservationStatus.CANCELLED
