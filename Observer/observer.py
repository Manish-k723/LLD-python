from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def update(self, temp: int) -> None:
        ...
