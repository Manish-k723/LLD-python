from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def notifyUser(self, message: str) -> None:
        ...

    @abstractmethod
    def notifyDriver(self, message) -> None:
        ...