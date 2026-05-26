from __future__ import annotations

from Notification.notification_methods import NotificationMethod
from Notification.notification_service import NotificationService
from Notification.user import User


class NotificationController:
    def __init__(self, notification_service: NotificationService):
        self._notification_service = notification_service

    def send_user_notification(
        self,
        user: User,
        message: str,
        template_name: str | None = None,
    ) -> int:
        return self._notification_service.send_user_notification(user, message, template_name)

    def send_campaign_notification(
        self,
        campaign_id: int,
        campaign_name: str,
        message: str,
        channels: list[NotificationMethod],
        template_name: str | None = None,
    ) -> int:
        return self._notification_service.send_campaign_notification(
            campaign_id=campaign_id,
            campaign_name=campaign_name,
            message=message,
            channels=channels,
            template_name=template_name,
        )
