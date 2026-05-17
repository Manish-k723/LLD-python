from datetime import datetime

from CabBooking.trip import Trip


class TripService:
    def get_trip(self) -> Trip:
        return self.__trip

    def book_trip(self, user, driver, notification_strategy, origin, destination):
        trip = Trip(1, driver, user, notification_strategy, origin, destination, datetime.now())
        self.__trip = trip
        notification_strategy.notify_trip_booking(
            f"Trip booked with {driver.get_name()} for {user.get_name()}"
        )

    def end_trip(self):
        pass

    def cancel_trip(self):
        pass

    def assign_driver(self):
        pass
