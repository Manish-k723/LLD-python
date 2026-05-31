from event import Event
from location import Location

class EventService:
    def __init__(self):
        self.events: dict[str, Event] = {}

    def create_event(self, user_id: int):
        event: Event = Event(
            title = "New Event",
            user_id = user_id,
            description = "This is a new event",
            start_time = "2023-01-01 10:00:00",
            end_time = "2023-01-01 12:00:00",
            location = Location("virtual", "100"),

        )