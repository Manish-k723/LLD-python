from CabBooking.notification_strategy import NotificationStrategy


class NotificationService:
    def __init__(self, notification_strategy: NotificationStrategy):
        self.__notification_strategy = notification_strategy

    def notify_rider(self, message: str) -> None:
        self.__notification_strategy.notify_rider(message)

    def notify_driver(self, message: str) -> None:
        self.__notification_strategy.notify_driver(message)