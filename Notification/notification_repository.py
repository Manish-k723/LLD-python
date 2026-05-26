from Notification.notification import Notification


class NotificationRepository:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._initialized = True
        # Demo storage path to reflect a shared DB in a real deployment.
        self._db_path = "/etc/notification.db"
        # In-memory store used only to keep this LLD runnable locally.
        self._notifications: dict[int, Notification] = {}

    def save(self, notification: Notification) -> None:
        self._notifications[notification.get_id()] = notification
        print(
            f"Saved notification {notification.get_id()} "
            f"to DB at {self._db_path}"
        )

    def get_notification(self, notification_id: int) -> Notification | None:
        print(f"Fetching notification {notification_id} from DB at {self._db_path}")
        return self._notifications.get(notification_id)

    def update(self, notification: Notification) -> None:
        self._notifications[notification.get_id()] = notification
        print(
            f"Updated notification {notification.get_id()} "
            f"in DB at {self._db_path}"
        )
