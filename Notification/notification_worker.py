import time

from Notification.notification_repository import NotificationRepository
from Notification.notification_sender import NotificationSender
from Notification.queue_processor import QueueProcessor


class NotificationWorker:
    def __init__(
        self,
        notification_repo: NotificationRepository,
        notification_sender: NotificationSender,
        queue_processor: QueueProcessor,
    ):
        self._notification_sender = notification_sender
        self._notification_repo = notification_repo
        self._queue_processor = queue_processor

    def process_notifications(self) -> None:
        while self._queue_processor.has_notifications():
            notification_id = self._queue_processor.get_next_notification()
            notification = self._notification_repo.get_notification(notification_id)

            if notification is None:
                print(f"Notification with id {notification_id} not found")
                continue

            is_sent = self._notification_sender.send_notification(notification)
            if is_sent:
                notification.mark_sent()
            elif notification.get_retry_count() > 0:
                notification.mark_retry()
                notification.reduce_retry_count()
                self._queue_processor.enqueue(notification.get_id())
            else:
                notification.mark_failed()
                self._queue_processor.add_to_dead_letter(notification.get_id())

            self._notification_repo.update(notification)
            time.sleep(10)
