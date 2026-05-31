from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from .enums import PermissionLevel, RSVPStatus
from .models import Event, Location, RecurrenceRule
from .services import (
    AvailabilityService,
    CalendarService,
    EventService,
    InvitationService,
    NotificationService,
    RecurrenceService,
    UserService,
)


class GoogleCalendarFacade:
    def __init__(self) -> None:
        self.users = UserService()
        self.calendars = CalendarService()
        self.events = EventService()
        self.availability = AvailabilityService(self.events)
        self.invitations = InvitationService()
        self.recurrence = RecurrenceService()
        self.notifications = NotificationService()

    def register_user(self, name: str, email: str) -> int:
        return self.users.create_user(name, email).id

    def create_calendar(self, owner_id: int, calendar_name: str) -> int:
        self.users.get(owner_id)
        return self.calendars.create_calendar(owner_id, calendar_name).id

    def schedule_event(
        self,
        calendar_id: int,
        created_by: int,
        title: str,
        start_time: datetime,
        end_time: datetime,
        attendee_ids: Optional[List[int]] = None,
        description: str = "",
        location: Optional[Location] = None,
        recurrence: Optional[RecurrenceRule] = None,
    ) -> Event:
        self.calendars.get(calendar_id)
        self.users.get(created_by)

        attendee_ids = attendee_ids or []
        all_people = [created_by, *attendee_ids]
        for uid in all_people:
            self.users.get(uid)
            if self.availability.has_conflict(uid, start_time, end_time):
                raise ValueError(f"User {uid} is not available in this time range")

        event = self.events.create_event(
            calendar_id=calendar_id,
            title=title,
            start_time=start_time,
            end_time=end_time,
            created_by=created_by,
            description=description,
            location=location,
            recurrence=recurrence,
        )
        self.invitations.invite(event, attendee_ids, PermissionLevel.VIEWER)
        self.notifications.send_event_created(event)
        return event

    def cancel_event(self, event_id: int) -> Event:
        event = self.events.cancel_event(event_id)
        self.notifications.send_event_cancelled(event)
        return event

    def respond_to_invite(self, event_id: int, user_id: int, status: RSVPStatus) -> Event:
        self.users.get(user_id)
        event = self.events.get(event_id)
        event.set_rsvp(user_id, status)
        self.notifications.send_rsvp_update(event, user_id, status)
        return event

    def list_events(self, calendar_id: int) -> List[Event]:
        self.calendars.get(calendar_id)
        return self.events.list_calendar_events(calendar_id)

    def event_occurrences(self, event_id: int):
        event = self.events.get(event_id)
        return self.recurrence.expand(event)
