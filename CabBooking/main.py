from CabBooking.cab import Cab
from CabBooking.cab_booking_service import CabBookingService
from CabBooking.cab_type import CabType
from CabBooking.driver import Driver
from CabBooking.location import Location
from CabBooking.payment_service import PaymentService
from CabBooking.rider import Rider
from CabBooking.email_notification_strategy import EmailNotificationStrategy
from CabBooking.upi_payment_strategy import UpiPaymentStrategy


def build_platform():
    riders = [
        Rider(1, "Manish", "8800640001", Location(12, 56)),
        Rider(2, "Penka", "85958000043", Location(18, 60)),
    ]

    cab1 = Cab(1, CabType.HATCHBACK, "DL1A1111")
    cab2 = Cab(2, CabType.SEDAN, "DL1A2222")
    cab3 = Cab(3, CabType.SUV, "DL1A3333")

    drivers = [
        Driver(101, "Suresh", "9000000001", Location(11, 56), cab1),
        Driver(102, "Mahesh", "9000000001", Location(20, 12), cab2),
        Driver(103, "Amit", "9000000003", Location(18, 60), cab3),
    ]

    return CabBookingService(riders,
                             drivers,
                             EmailNotificationStrategy(),
                             PaymentService(UpiPaymentStrategy()))

cab_booking_service = build_platform()
pickup = Location(12, 56)
available_drivers = cab_booking_service.search_cab(pickup)

for driver in available_drivers:
    print(driver.get_name(), driver.get_cab().get_cab_type())

trip1 = cab_booking_service.book_cab(1, pickup, CabType.SEDAN,  Location(1500000, 50))
trip2 = cab_booking_service.book_cab(2, pickup, CabType.HATCHBACK, Location(1500000, 50))
if not trip1:
    print("Booking failed")
else:
    print(f"Trip booked: {trip1.get_trip_id()}, fare={trip1.get_estimated_fare():.2f}")
    cab_booking_service.start_trip(trip1.get_trip_id())
    cab_booking_service.complete_trip(trip1.get_trip_id())

if not trip2:
    print("Booking failed for second trip")
else:
    print(f"Trip booked: {trip2.get_trip_id()}, fare={trip2.get_estimated_fare():.2f}")
    cab_booking_service.start_trip(trip2.get_trip_id())
    cab_booking_service.complete_trip(trip2.get_trip_id())

