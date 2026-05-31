from __future__ import annotations

from Tinder.enums import Gender
from Tinder.user_preference import Interest


class UserProfile:
    def __init__(self, name: str, age: int, gender: Gender, bio: str | None = None):
        self._name = name
        self._age = age
        self._gender: Gender = gender
        self._bio: str | None = bio
        self._photos: list[str] = []
        self._interests: list[Interest] = []

    def get_gender(self) -> Gender:
        return self._gender

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def get_bio(self) -> str | None:
        return self._bio

    def add_interest(self, interest: list[Interest]):
        self._interests.extend(interest)