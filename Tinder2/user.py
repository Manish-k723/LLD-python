from __future__ import annotations

from Tinder2.enums import Gender
from Tinder2.location import Location
from Tinder2.user_preference import UserPreference
from Tinder2.user_profile import UserProfile


class User:
    _next_id = 1

    def __init__(self, name: str, age: int, gender: Gender, location: Location):
        self._id = User._next_id
        User._next_id += 1

        self._profile = UserProfile(name, age, gender)
        self._preferences = UserPreference()
        self._location = location
        self._match_history: list[int] = []

    def get_id(self) -> int:
        return self._id

    def get_user_profile(self) -> UserProfile:
        return self._profile

    def get_user_preferences(self) -> UserPreference:
        return self._preferences

    def get_location(self) -> Location:
        return self._location

    def add_match(self, match_id: int) -> None:
        self._match_history.append(match_id)
