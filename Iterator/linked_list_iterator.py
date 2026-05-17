from __future__ import annotations

from iterator import Iterator
from node import Node
from song import Song


class LinkedListIterator(Iterator):
    def __init__(self, head: Node | None):
        self._current = head

    def has_next(self) -> bool:
        return self._current is not None

    def next(self) -> Song:
        if not self.has_next():
            raise StopIteration

        song = self._current.value
        self._current = self._current.next
        return song
