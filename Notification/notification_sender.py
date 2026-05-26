from Notification.notification import Notification
from Notification.notification_strategy_factory import NotificationStrategyFactory


class NotificationSender:
    def send_notification(self, notification: Notification) -> bool:
        if not notification.get_channels():
            return False

        all_channels_sent = True
        for channel in notification.get_channels():
            strategy = NotificationStrategyFactory.create_strategy(channel)
            if strategy is None:
                all_channels_sent = False
                continue
            sent = strategy.notify(notification)
            all_channels_sent = all_channels_sent and sent
        return all_channels_sent
