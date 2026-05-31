from Tinder.enums import Gender
from dataclasses import dataclass

@dataclass
class Interest:
    _name: str
    _category: str

class UserPreference:
    def __init__(self, distance: int, max_age: int= None, min_age: int= None):
        self._distance = distance
        self._max_age = max_age
        self._min_age = min_age
        self._gender: list[Gender] = []

    def get_max_age(self):
        return self._max_age
    def get_min_age(self):
        return self._min_age
    def get_gender(self) -> list[Gender]:
        return self._gender
    def get_distance(self):
        return self._distance
    def add_gender(self, gender: Gender):
        self._gender.append(gender)

    def set_min_age(self, min_age: int) -> None:
        self._min_age = min_age
    def set_max_age(self, max_age: int) -> None:
        self._max_age = max_age
    def set_distance(self, distance: int) -> None:
        self._distance = distance
