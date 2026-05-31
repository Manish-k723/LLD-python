from dataclasses import dataclass
from datetime import datetime

from Tinder.notification import NotificationService, NotificationStrategy


@dataclass
class Match:
    id: int
    user1: int
    user2: int
    matched_at: datetime

    def __str__(self):
        return f"Match {self.id} between users {self.user1} and {self.user2} at {self.matched_at}"

class MatchService:
    def __init__(self):
        self._next_match_id = 1
        self._matches: dict[int, Match] = {}

    def create_match(self, user1: int, user2: int):
        match = Match(self._next_match_id, user1, user2, datetime.now())
        self._matches[self._next_match_id] = match
        self._next_match_id += 1
        return match

    def get_matches(self):
        return self._matches.values()

