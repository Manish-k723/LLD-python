from notification_strategy import NotificationStrategy

class EmailNotificationStrategy(NotificationStrategy):
    def notifyUser(self, message: str) -> None:
        print(f"Email sent to user: {message}")

    def notifyDriver(self, message: str) -> None:
        print(f"Email sent to driver: {message}")