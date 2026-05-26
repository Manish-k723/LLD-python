from Notification.preference import Preference


class User:
    _next_id = 1

    def __init__(self, name: str, email: str, phone: str | None = None):
        self._id = User._next_id
        User._next_id += 1
        self._name = name
        self._email = email
        self._phone = phone
        self._preferences: list[Preference] = []

    def add_preference(self, preference: Preference) -> None:
        self._preferences.append(preference)

    def remove_preference(self, preference: Preference) -> None:
        self._preferences.remove(preference)

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def get_phone(self) -> str | None:
        return self._phone

    def get_preferences(self) -> list[Preference]:
        return list(self._preferences)
