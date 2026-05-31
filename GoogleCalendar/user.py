from GoogleCalendar.calendar import Calendar

class User:
    _next_id = 1
    def __init__(self, name: str, email: str):
        self._id = User._next_id
        User._next_id += 1

        self._name = name
        self._email = email
        self.calendars: list[Calendar] = []