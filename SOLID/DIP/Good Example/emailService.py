from notificationChannel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")
        