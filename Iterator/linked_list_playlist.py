from __future__ import annotations

from linked_list_iterator import LinkedListIterator
from node import Node
from song import Song


class LinkedListPlaylist:
    def __init__(self):
        self._head: Node | None = None
        self._tail: Node | None = None

    def add_song(self, song: Song) -> None:
        new_node = Node(song)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            return

        self._tail.next = new_node
        self._tail = new_node

    def create_iterator(self) -> LinkedListIterator:
        return LinkedListIterator(self._head)
