from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_cost(self) -> float:
        pass

class Coffee(Beverage):
    def get_description(self) -> str:
        return "Plain Coffee"

    def get_cost(self) -> float:
        return 150

class AddOnDecorator(Beverage):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee
    def get_description(self) -> str:
        ...

    def get_cost(self) -> float:
        ...

class MilkOnDecorator(AddOnDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} with Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 50

class WhipCreamDecorator(AddOnDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} with WhipCream"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 30

class SugarDecorator(AddOnDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} with Sugar"

    def get_cost(self) -> float:
        return self._coffee.get_cost() - 100

coffee = Coffee()
coffee = MilkOnDecorator(WhipCreamDecorator(SugarDecorator(coffee)))
print(coffee.get_description())
print(coffee.get_cost())