from iterator import Iterator
from typing import List
from song import Song

class ListIterator(Iterator):
    def __init__(self, items: List[Song]) -> None:
        self.items: List[Song] = items
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.items)

    def next(self) -> Song:
        if not self.has_next():
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item
