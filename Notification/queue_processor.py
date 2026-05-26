from collections import deque


class QueueProcessor:
    def __init__(self):
        self._queue: deque[int] = deque()
        self._dead_letter_queue: deque[int] = deque()

    def enqueue(self, notification_id: int) -> None:
        self._queue.append(notification_id)

    def add_to_dead_letter(self, notification_id: int) -> None:
        self._dead_letter_queue.append(notification_id)

    def get_next_notification(self) -> int:
        return self._queue.popleft()

    def has_notifications(self) -> bool:
        return len(self._queue) > 0

    def get_dead_letters(self) -> list[int]:
        return list(self._dead_letter_queue)
