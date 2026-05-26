from __future__ import annotations

from typing import TYPE_CHECKING

from Notification.notification_methods import NotificationMethod
from Notification.notification_priority import NotificationPriority

if TYPE_CHECKING:
    from Notification.user import User


class Preference:
    def __init__(
        self,
        priority: NotificationPriority,
        channels: list[NotificationMethod],
    ):
        self._priority = priority
        self._channels = channels

    def applies_to(self, priority: NotificationPriority) -> bool:
        return self._priority == priority

    def get_channels(self) -> list[NotificationMethod]:
        return list(self._channels)


class PreferenceService:
    def get_notification_priority(self, message: str) -> NotificationPriority:
        lowered_message = message.lower()
        if "otp" in lowered_message or "urgent" in lowered_message:
            return NotificationPriority.CRITICAL
        if "reminder" in lowered_message or "alert" in lowered_message:
            return NotificationPriority.SEMI_CRITICAL
        return NotificationPriority.NON_CRITICAL

    def get_channels_for_user(
        self,
        user: User,
        priority: NotificationPriority,
    ) -> list[NotificationMethod]:
        for preference in user.get_preferences():
            if preference.applies_to(priority):
                return preference.get_channels()

        return [NotificationMethod.EMAIL]
