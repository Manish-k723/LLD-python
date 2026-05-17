from abc import ABC, abstractmethod
from song import Song

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        ...
    @abstractmethod
    def next(self) -> Song:
        ...