from Notification.client import Client
from Notification.notification_controller import NotificationController
from Notification.notification_methods import NotificationMethod
from Notification.notification_priority import NotificationPriority
from Notification.notification_repository import NotificationRepository
from Notification.notification_sender import NotificationSender
from Notification.notification_service import NotificationService
from Notification.notification_worker import NotificationWorker
from Notification.preference import Preference, PreferenceService
from Notification.queue_processor import QueueProcessor
from Notification.template import TemplateService
from Notification.user import User


def main() -> None:
    notification_repo = NotificationRepository()
    queue_processor = QueueProcessor()
    template_service = TemplateService()
    preference_service = PreferenceService()
    notification_sender = NotificationSender()

    notification_service = NotificationService(
        template_service=template_service,
        notification_repo=notification_repo,
        queue_processor=queue_processor,
        preference_service=preference_service,
    )
    notification_controller = NotificationController(notification_service)
    notification_worker = NotificationWorker(
        notification_repo=notification_repo,
        notification_sender=notification_sender,
        queue_processor=queue_processor,
    )

    client = Client("Marketing Console", notification_controller)

    user = User(name="Manish", email="manish@example.com", phone="+911234567890")
    user.add_preference(
        Preference(
            NotificationPriority.CRITICAL,
            [NotificationMethod.SMS, NotificationMethod.EMAIL],
        )
    )
    user.add_preference(
        Preference(
            NotificationPriority.SEMI_CRITICAL,
            [NotificationMethod.PUSH, NotificationMethod.EMAIL],
        )
    )

    user_notification_id = client.send_user_notification(
        user=user,
        message="Your OTP is 123456",
        template_name="alert",
    )
    print(f"Queued user notification {user_notification_id}")

    campaign_notification_id = client.send_campaign_notification(
        campaign_id=101,
        campaign_name="Summer Sale",
        message="50% off on all plans today only",
        channels=[NotificationMethod.EMAIL, NotificationMethod.PUSH],
        template_name="campaign",
    )
    print(f"Queued campaign notification {campaign_notification_id}")

    notification_worker.process_notifications()

    user_notification = notification_repo.get_notification(user_notification_id)
    campaign_notification = notification_repo.get_notification(campaign_notification_id)
    print(f"Final status for user notification {user_notification_id}: {user_notification.get_status().value}")
    print(
        f"Final status for campaign notification {campaign_notification_id}: "
        f"{campaign_notification.get_status().value}"
    )


if __name__ == "__main__":
    main()
