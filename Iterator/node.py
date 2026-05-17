from __future__ import annotations

from song import Song


class Node:
    def __init__(self, value: Song):
        self.value = value
        self.next: Node | None = None
