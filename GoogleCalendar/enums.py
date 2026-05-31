from enum import Enum

class EventStatus(Enum):
    TENTATIVE = "tentative"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class RecurringFrequency(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

class PermissionLevel(Enum):
    OWNER = "owner"
    EDITOR = "editor"
    NONE = "none"

class UserStatus(Enum):
    FREE = "free"
    BUSY = "busy"
    DECLINED = "declined"

