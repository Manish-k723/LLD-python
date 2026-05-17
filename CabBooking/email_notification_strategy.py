from notification_strategy import NotificationStrategy


class EmailNotificationStrategy(NotificationStrategy):
    def notify_rider(self, message: str) -> None:
        print(f"Email to rider: {message}")

    def notify_driver(self, message: str) -> None:
        print(f"Email to driver: {message}")
