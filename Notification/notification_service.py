from __future__ import annotations

from Notification.notification_factory import NotificationFactory
from Notification.notification_methods import NotificationMethod
from Notification.notification_repository import NotificationRepository
from Notification.preference import PreferenceService
from Notification.queue_processor import QueueProcessor
from Notification.template import TemplateService
from Notification.user import User


class NotificationService:
    def __init__(
        self,
        template_service: TemplateService,
        notification_repo: NotificationRepository,
        queue_processor: QueueProcessor,
        preference_service: PreferenceService,
    ):
        self._template_service = template_service
        self._notification_repo = notification_repo
        self._queue_processor = queue_processor
        self._preference_service = preference_service

    def send_user_notification(
        self,
        user: User,
        message: str,
        template_name: str | None = None,
    ) -> int:
        priority = self._preference_service.get_notification_priority(message)
        channels = self._preference_service.get_channels_for_user(user, priority)
        template = self._template_service.get_template(priority, template_name)
        rendered_message = template.render(
            recipient_name=user.get_name(),
            message=message,
        )

        notification = NotificationFactory.create_user_notification(
            user=user,
            priority=priority,
            message=message,
            rendered_message=rendered_message,
            template_name=template.get_name(),
            channels=channels,
        )
        return self._queue_notification(notification)

    def send_campaign_notification(
        self,
        campaign_id: int,
        campaign_name: str,
        message: str,
        channels: list[NotificationMethod],
        template_name: str | None = None,
    ) -> int:
        priority = self._preference_service.get_notification_priority(message)
        template = self._template_service.get_template(priority, template_name)
        rendered_message = template.render(
            recipient_name=campaign_name,
            message=message,
        )

        notification = NotificationFactory.create_campaign_notification(
            campaign_id=campaign_id,
            priority=priority,
            message=message,
            rendered_message=rendered_message,
            template_name=template.get_name(),
            channels=channels,
        )
        return self._queue_notification(notification)

    def _queue_notification(self, notification) -> int:
        self._notification_repo.save(notification)
        self._queue_processor.enqueue(notification.get_id())
        return notification.get_id()
