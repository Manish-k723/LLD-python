from datetime import datetime

from Notification.notification_methods import NotificationMethod
from Notification.notification_priority import NotificationPriority
from Notification.notification_status import NotificationStatus


class Notification:
    _next_id = 1

    def __init__(
        self,
        message: str,
        rendered_message: str,
        template_name: str,
        retry_count: int,
        priority: NotificationPriority,
        channels: list[NotificationMethod],
    ):
        self._id = Notification._next_id
        Notification._next_id += 1
        self._message = message
        self._rendered_message = rendered_message
        self._status = NotificationStatus.PENDING
        self._created_at = datetime.now()
        self._template_name = template_name
        self._retry_count = retry_count
        self._priority = priority
        self._channels = channels

    def mark_sent(self) -> None:
        self._status = NotificationStatus.SENT

    def mark_failed(self) -> None:
        self._status = NotificationStatus.FAILED

    def mark_retry(self) -> None:
        self._status = NotificationStatus.RETRY

    def get_retry_count(self) -> int:
        return self._retry_count

    def reduce_retry_count(self) -> None:
        self._retry_count -= 1

    def get_id(self) -> int:
        return self._id

    def get_message(self) -> str:
        return self._message

    def get_rendered_message(self) -> str:
        return self._rendered_message

    def get_status(self) -> NotificationStatus:
        return self._status

    def get_created_at(self) -> datetime:
        return self._created_at

    def get_template_name(self) -> str:
        return self._template_name

    def get_channels(self) -> list[NotificationMethod]:
        return list(self._channels)

    def get_priority(self) -> NotificationPriority:
        return self._priority

    def __str__(self) -> str:
        return (
            f"Notification(id={self._id}, status={self._status.value}, "
            f"priority={self._priority.name}, channels={[channel.value for channel in self._channels]})"
        )


class UserNotification(Notification):
    def __init__(
        self,
        message: str,
        rendered_message: str,
        template_name: str,
        retry_count: int,
        priority: NotificationPriority,
        channels: list[NotificationMethod],
        user_id: int,
    ):
        super().__init__(
            message=message,
            rendered_message=rendered_message,
            template_name=template_name,
            retry_count=retry_count,
            priority=priority,
            channels=channels,
        )
        self._user_id = user_id

    def get_user_id(self) -> int:
        return self._user_id


class NotificationCampaign(Notification):
    def __init__(
        self,
        message: str,
        rendered_message: str,
        template_name: str,
        priority: NotificationPriority,
        channels: list[NotificationMethod],
        campaign_id: int,
    ):
        super().__init__(
            message=message,
            rendered_message=rendered_message,
            template_name=template_name,
            retry_count=0,
            priority=priority,
            channels=channels,
        )
        self._campaign_id = campaign_id

    def get_campaign_id(self) -> int:
        return self._campaign_id
