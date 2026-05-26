from Notification.notification import NotificationCampaign, UserNotification
from Notification.notification_methods import NotificationMethod
from Notification.notification_priority import NotificationPriority
from Notification.user import User


class NotificationFactory:
    @staticmethod
    def create_user_notification(
        user: User,
        priority: NotificationPriority,
        message: str,
        rendered_message: str,
        template_name: str,
        channels: list[NotificationMethod],
    ) -> UserNotification:
        retry_count = {
            NotificationPriority.CRITICAL: 2,
            NotificationPriority.SEMI_CRITICAL: 1,
            NotificationPriority.NON_CRITICAL: 0,
        }[priority]
        return UserNotification(
            message=message,
            rendered_message=rendered_message,
            template_name=template_name,
            retry_count=retry_count,
            priority=priority,
            channels=channels,
            user_id=user.get_id(),
        )

    @staticmethod
    def create_campaign_notification(
        campaign_id: int,
        priority: NotificationPriority,
        message: str,
        rendered_message: str,
        template_name: str,
        channels: list[NotificationMethod],
    ) -> NotificationCampaign:
        return NotificationCampaign(
            message=message,
            rendered_message=rendered_message,
            template_name=template_name,
            priority=priority,
            channels=channels,
            campaign_id=campaign_id,
        )
