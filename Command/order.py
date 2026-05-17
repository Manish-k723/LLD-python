from chef import Chef
from abc import ABC, abstractmethod

class Order(ABC):

    @abstractmethod
    def cook(self) -> None:
        ...

