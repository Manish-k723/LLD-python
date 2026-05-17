from CabBooking.cab_booking_service import CabBookingService
from CabBooking.email_notification_strategy import EmailNotificationStrategy
from CabBooking.location import Location
from CabBooking.rider import Rider

rider_location = Location(12, 56, "Najafgarh")
rider = Rider(1, "Manish", 880064, rider_location)

cab_booking = CabBookingService(EmailNotificationStrategy(), rider)
dropped_off_location = Location(14, 50, "Kapashera")

get_available_drivers = cab_booking.search_cab(rider_location, dropped_off_location)
cab_booking.book_cab(get_available_drivers[1], rider_location, dropped_off_location)
