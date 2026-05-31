from __future__ import annotations

from Tinder2.enums import Gender
from Tinder2.user_preference import Interest


class UserProfile:
    def __init__(self, name: str, age: int, gender: Gender, bio: str | None = None):
        self._name = name
        self._age = age
        self._gender = gender
        self._bio = bio
        self._interests: list[Interest] = []

    def get_age(self) -> int:
        return self._age

    def get_gender(self) -> Gender:
        return self._gender

    def get_interests(self) -> list[Interest]:
        return list(self._interests)

    def add_interest(self, interest: Interest) -> None:
        self._interests.append(interest)

