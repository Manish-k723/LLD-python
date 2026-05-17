from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self):
        ...