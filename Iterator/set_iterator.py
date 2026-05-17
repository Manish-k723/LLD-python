from __future__ import annotations

from iterator import Iterator
from typing import Set, List
from song import Song

class SetIterator(Iterator):
    def __init__(self, items: Set[Song]):
        self.items: List[Song] = list(items)
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.items)

    def next(self) -> Song | None:
        if not self.has_next():
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item
