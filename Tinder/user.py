from Tinder.enums import Gender
from Tinder.location import Location
from Tinder.user_preference import UserPreference
from Tinder.user_profile import UserProfile


class User:
    _next_id = 1
    def __init__(self, name: str, age: int, gender: Gender, location: Location):
        self._id = User._next_id
        User._next_id += 1
        self._match_history = []

        self._user_profile = UserProfile(name, age, gender)
        self._user_preferences = UserPreference(5)

        # self._swipe_history: dict[int, int] = {}
        self._location = location

    def add_match(self, match):
        self._match_history.append(match)

    def get_id(self):
        return self._id

    def get_gender(self) -> Gender:
        return self._user_profile.get_gender()

    def get_user_profile(self) -> UserProfile:
        return self._user_profile

    def get_location(self) -> Location:
        return self._location

    def get_user_preferences(self) -> UserPreference:
        return self._user_preferences

    def get_name(self):
        return self._user_profile.get_name()

