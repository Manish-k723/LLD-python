from Notification.notification_controller import NotificationController
from Notification.notification_methods import NotificationMethod
from Notification.user import User


class Client:
    _next_id = 1

    def __init__(self, name: str, notification_controller: NotificationController):
        self._id = Client._next_id
        Client._next_id += 1
        self._name = name
        self._notification_controller = notification_controller

    def send_user_notification(
        self,
        user: User,
        message: str,
        template_name: str | None = None,
    ) -> int:
        return self._notification_controller.send_user_notification(
            user=user,
            message=message,
            template_name=template_name,
        )

    def send_campaign_notification(
        self,
        campaign_id: int,
        campaign_name: str,
        message: str,
        channels: list[NotificationMethod],
        template_name: str | None = None,
    ) -> int:
        return self._notification_controller.send_campaign_notification(
            campaign_id=campaign_id,
            campaign_name=campaign_name,
            message=message,
            channels=channels,
            template_name=template_name,
        )
