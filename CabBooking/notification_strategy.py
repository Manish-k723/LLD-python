from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    @abstractmethod
    def notify_rider(self, message: str) -> None:
        ...

    @abstractmethod
    def notify_driver(self, message: str) -> None:
        ...
