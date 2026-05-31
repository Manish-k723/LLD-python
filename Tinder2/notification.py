from __future__ import annotations


class NotificationService:
    def send_notification(self, user_id: int, message: str) -> None:
        print(f"Notify user {user_id}: {message}")

