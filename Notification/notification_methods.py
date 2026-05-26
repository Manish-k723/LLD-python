from enum import Enum

class NotificationMethod(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"