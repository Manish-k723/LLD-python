from abc import ABC, abstractmethod

class NotificationService:
    def __init__(self, notification_strategy: NotificationStrategy):
        self._notification_strategy = notification_strategy

    def send_notification(self, user: int, message: str):
        self._notification_strategy.notify(user, message)

class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, user: int, message: str):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def notify(self, user: int, message: str):
        print(f"Sending email: {message} to User {user}")

class InAppNotificationStrategy(NotificationStrategy):
    def notify(self, user: int, message: str):
        print(f"Sending Push message: {message} to User {user}")