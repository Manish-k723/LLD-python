class Engine:
    def __init__(self, cylinders: int, hp: int) -> None:
        self.__cylinders = cylinders
        self.__horsepower = hp

    def get_horsepower(self) -> int:
        return self.__horsepower

    def get_cylinders(self) -> int:
        return self.__cylinders

    def start_engine(self) -> None:
        print("Vroom Vroom")

class Car:
    def __init__(self, model: str, cylinders: int, hp: int) -> None:
        self.__model = model
        self.__engine = Engine(cylinders, hp)

    def get_engine(self) -> Engine:
        return self.__engine

    def get_details(self) -> str:
        return f"{self.__model} has {self.__engine.get_horsepower()} hp engine"

    def start_car(self) -> None:
        self.__engine.start_engine()

car = Car("BMW", 5, 150)
print(car.get_details())
