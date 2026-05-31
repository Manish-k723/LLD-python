from typing import List

from GoogleCalendar.event import Event


class CalendarService:
    def __init__(self):
        self._event_service = None
        self._recurrence_service = None
        self._invitation_service = None
        self._notification_service = None
        self._events: dict[int, Event] = {}

    def create_event(self):
        event = self._event_service.create_event()
        self._invitation_service.send_invitations(event)
        self._recurrence_service.setup_recurrence(event)
        self._notification_service.notify_subscribers(event)
        self._events[event.get_id()] = event
        return event
    def get_events(self) -> List[Event]:
        return list(self._events.values())

    def update_event(self, event_id: int):
        event = self._events.get(event_id)



