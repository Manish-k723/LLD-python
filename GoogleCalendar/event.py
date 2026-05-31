from datetime import datetime
from asyncio import Lock
from location import Location

from enums import *

class Event:
    _next_id = 1
    def __init__(self, title: str, user_id: int, start_time: datetime, end_time: datetime, location: Location, description: str):
        self._id = Event._next_id
        Event._next_id += 1

        self._title = title
        self._start_time = start_time
        self._end_time = end_time
        self._location = location
        self._description = description
        self._status = EventStatus.TENTATIVE
        self._owner = user_id
        self._updated_by = user_id
        self._created_by = user_id
        self._attendees = []
        self._recurrence = None
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self.permission: dict[int, PermissionLevel] = {}
        self._lock = Lock()

    def add_attendee(self, user_id: int, permission: PermissionLevel):
        with self._lock:
            self._attendees.append(user_id)
            self.permission[user_id] = permission

    def set_recurring_rule(self, recurrence: str):
        self._recurrence = recurrence


