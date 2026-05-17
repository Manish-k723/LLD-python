class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age

    def __eat(self) -> None:
        print("nom nom nom")

    def sleep(self) -> None:
        print("zzzzzz")

    @property
    def age(self):
        return self._age


class Dog(Animal):
    def __init__(self, name, age, breed) -> None:
        super().__init__(name, age)
        self.__breed = breed

    def eat(self) -> None:
        super()._Animal__eat()
        print("chik chik")

    def bark(self) -> None:
        print(f"woof woof by {self.name}")

dog = Dog("Chhoti", 1, "Pomeranian")
dog.eat()
dog.bark()
print(dog.age)
print(dog._Dog__breed)