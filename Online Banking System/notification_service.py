from typing import List

from notification_channel import *
class NotificationService:
    def __init__(self):
        self._channel: List[NotificationChannel] = []

    def add_notification_channel(self, notification_channel: NotificationChannel):
        self._channel.append(notification_channel)

    def notify(self, message: str):
        for channel in self._channel:
            channel.send(message)
    
