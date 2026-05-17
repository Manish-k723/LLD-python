from notificationChannel import NotificationChannel

class SmsService(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")
