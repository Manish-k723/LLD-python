from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Dict, List, Optional

from .enums import EventStatus, PermissionLevel, RSVPStatus, RecurringFrequency


@dataclass(frozen=True)
class Location:
    name: str
    capacity: int = 0


@dataclass
class RecurrenceRule:
    frequency: RecurringFrequency
    interval: int = 1
    count: Optional[int] = None


@dataclass
class User:
    id: int
    name: str
    email: str


@dataclass
class Calendar:
    id: int
    owner_id: int
    name: str


@dataclass
class Event:
    id: int
    calendar_id: int
    title: str
    start_time: datetime
    end_time: datetime
    created_by: int
    location: Optional[Location] = None
    description: str = ""
    status: EventStatus = EventStatus.TENTATIVE
    recurrence: Optional[RecurrenceRule] = None
    attendees: List[int] = field(default_factory=list)
    permissions: Dict[int, PermissionLevel] = field(default_factory=dict)
    rsvp: Dict[int, RSVPStatus] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    _lock: Lock = field(default_factory=Lock, repr=False)

    def add_attendee(self, user_id: int, permission: PermissionLevel = PermissionLevel.VIEWER) -> None:
        with self._lock:
            if user_id not in self.attendees:
                self.attendees.append(user_id)
            self.permissions[user_id] = permission
            self.rsvp.setdefault(user_id, RSVPStatus.PENDING)
            self.updated_at = datetime.utcnow()

    def set_rsvp(self, user_id: int, status: RSVPStatus) -> None:
        with self._lock:
            if user_id not in self.attendees:
                raise ValueError(f"User {user_id} is not an attendee")
            self.rsvp[user_id] = status
            self.updated_at = datetime.utcnow()
