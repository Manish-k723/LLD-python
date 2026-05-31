from __future__ import annotations

from datetime import timedelta
from typing import Dict, List, Optional

from .enums import EventStatus, PermissionLevel, RSVPStatus, RecurringFrequency
from .models import Calendar, Event, Location, RecurrenceRule, User


class UserService:
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}
        self._next_id = 1

    def create_user(self, name: str, email: str) -> User:
        user = User(id=self._next_id, name=name, email=email)
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> User:
        user = self._users.get(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return user


class CalendarService:
    def __init__(self) -> None:
        self._calendars: Dict[int, Calendar] = {}
        self._next_id = 1

    def create_calendar(self, owner_id: int, name: str) -> Calendar:
        cal = Calendar(id=self._next_id, owner_id=owner_id, name=name)
        self._calendars[self._next_id] = cal
        self._next_id += 1
        return cal

    def get(self, calendar_id: int) -> Calendar:
        cal = self._calendars.get(calendar_id)
        if not cal:
            raise ValueError(f"Calendar {calendar_id} not found")
        return cal


class EventService:
    def __init__(self) -> None:
        self._events: Dict[int, Event] = {}
        self._by_calendar: Dict[int, List[int]] = {}
        self._next_id = 1

    def create_event(
        self,
        calendar_id: int,
        title: str,
        start_time,
        end_time,
        created_by: int,
        description: str = "",
        location: Optional[Location] = None,
        recurrence: Optional[RecurrenceRule] = None,
    ) -> Event:
        if end_time <= start_time:
            raise ValueError("end_time must be after start_time")

        event = Event(
            id=self._next_id,
            calendar_id=calendar_id,
            title=title,
            start_time=start_time,
            end_time=end_time,
            created_by=created_by,
            description=description,
            location=location,
            recurrence=recurrence,
            permissions={created_by: PermissionLevel.OWNER},
        )
        self._events[self._next_id] = event
        self._by_calendar.setdefault(calendar_id, []).append(self._next_id)
        self._next_id += 1
        return event

    def get(self, event_id: int) -> Event:
        event = self._events.get(event_id)
        if not event:
            raise ValueError(f"Event {event_id} not found")
        return event

    def list_calendar_events(self, calendar_id: int) -> List[Event]:
        return [self._events[eid] for eid in self._by_calendar.get(calendar_id, [])]

    def cancel_event(self, event_id: int) -> Event:
        event = self.get(event_id)
        event.status = EventStatus.CANCELLED
        return event


class AvailabilityService:
    def __init__(self, event_service: EventService) -> None:
        self._event_service = event_service

    def has_conflict(self, user_id: int, start_time, end_time, ignore_event_id: Optional[int] = None) -> bool:
        for event in self._event_service._events.values():
            if ignore_event_id == event.id:
                continue
            participants = [event.created_by, *event.attendees]
            if user_id not in participants:
                continue
            if event.status == EventStatus.CANCELLED:
                continue
            overlaps = not (end_time <= event.start_time or start_time >= event.end_time)
            if overlaps:
                return True
        return False


class InvitationService:
    def invite(self, event: Event, attendee_ids: List[int], permission: PermissionLevel = PermissionLevel.VIEWER) -> None:
        for attendee_id in attendee_ids:
            event.add_attendee(attendee_id, permission)


class RecurrenceService:
    def expand(self, event: Event) -> List[tuple]:
        if not event.recurrence:
            return [(event.start_time, event.end_time)]

        rule = event.recurrence
        count = rule.count or 1
        step_map = {
            RecurringFrequency.DAILY: timedelta(days=rule.interval),
            RecurringFrequency.WEEKLY: timedelta(weeks=7 * rule.interval),
            RecurringFrequency.MONTHLY: timedelta(days=30 * rule.interval),
        }
        step = step_map[rule.frequency]

        out = []
        start = event.start_time
        end = event.end_time
        for _ in range(count):
            out.append((start, end))
            start += step
            end += step
        return out


class NotificationService:
    def send_event_created(self, event: Event) -> None:
        recipients = [event.created_by, *event.attendees]
        print(f"[Notify] Event {event.id} created for users: {recipients}")

    def send_event_cancelled(self, event: Event) -> None:
        recipients = [event.created_by, *event.attendees]
        print(f"[Notify] Event {event.id} cancelled for users: {recipients}")

    def send_rsvp_update(self, event: Event, user_id: int, status: RSVPStatus) -> None:
        print(f"[Notify] RSVP update for event {event.id}: user={user_id}, status={status.value}")
