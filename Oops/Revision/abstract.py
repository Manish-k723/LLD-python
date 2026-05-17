from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        print("perimeter")
        print(self.area())
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # super().area()
        return self.width * self.height

    def perimeter(self):
        # super().perimeter()
        return self.width * 2 + self.height * 2

rectangle = Rectangle(5, 2)
print(rectangle.area())
print(rectangle.perimeter())