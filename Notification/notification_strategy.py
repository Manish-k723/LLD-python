from abc import ABC, abstractmethod

from Notification.notification import Notification


class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, notification: Notification) -> bool:
        raise NotImplementedError


class EmailNotificationStrategy(NotificationStrategy):
    def notify(self, notification: Notification) -> bool:
        print(f"EMAIL sent: {notification.get_rendered_message()}")
        return True


class SMSNotificationStrategy(NotificationStrategy):
    def notify(self, notification: Notification) -> bool:
        print(f"SMS sent: {notification.get_rendered_message()}")
        return True


class PushNotificationStrategy(NotificationStrategy):
    def notify(self, notification: Notification) -> bool:
        print(f"PUSH sent: {notification.get_rendered_message()}")
        return True
