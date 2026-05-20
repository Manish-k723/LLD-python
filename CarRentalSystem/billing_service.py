from math import ceil

from reservation import Reservation


class BillingService:
    def calculate_amount(self, reservation: Reservation) -> float:
        duration_seconds = (reservation.get_end_time() - reservation.get_start_time()).total_seconds()
        hours = max(1, ceil(duration_seconds / 3600))
        return hours * reservation.get_vehicle().get_hourly_rate()
