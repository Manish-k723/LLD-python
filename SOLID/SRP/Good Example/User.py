class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def is_adult(self) -> bool:
        return self.age >= 18

