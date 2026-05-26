from abc import ABC, abstractmethod
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        ...

class Email(NotificationChannel):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SMS(NotificationChannel):
    def send(self, message: str):
        print(f"Sending SMS: {message}")
