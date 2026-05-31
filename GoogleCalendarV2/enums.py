from enum import Enum


class EventStatus(Enum):
    TENTATIVE = "tentative"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class RecurringFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class PermissionLevel(Enum):
    OWNER = "owner"
    EDITOR = "editor"
    VIEWER = "viewer"


class RSVPStatus(Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
