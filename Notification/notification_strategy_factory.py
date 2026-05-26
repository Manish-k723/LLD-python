from __future__ import annotations

from Notification.notification_methods import NotificationMethod
from Notification.notification_strategy import (
    EmailNotificationStrategy,
    NotificationStrategy,
    PushNotificationStrategy,
    SMSNotificationStrategy,
)


class NotificationStrategyFactory:
    @staticmethod
    def create_strategy(channel: NotificationMethod) -> NotificationStrategy | None:
        if channel == NotificationMethod.EMAIL:
            return EmailNotificationStrategy()
        if channel == NotificationMethod.SMS:
            return SMSNotificationStrategy()
        if channel == NotificationMethod.PUSH:
            return PushNotificationStrategy()
        return None
