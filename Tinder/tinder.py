from __future__ import annotations

from Tinder.enums import SwipeAction
from Tinder.match import Match, MatchService
from Tinder.matcher import MatchEvaluator, build_matcher
from Tinder.notification import NotificationService, InAppNotificationStrategy
from Tinder.swipe import Swipe
from Tinder.user import User
import logging

logger = logging.getLogger(__name__)


class Tinder:
    def __init__(self, matcher: MatchEvaluator | None = None):
        self._user: dict[int, User] = {}
        self._matches_by_pair: dict[tuple[int, int], int] = {}
        self._swipes: dict[tuple[int, int], Swipe] = {}

        self._next_user_id = 1
        self._matcher: MatchEvaluator | None =  matcher or build_matcher()
        self._notification_service = NotificationService(InAppNotificationStrategy())
        self._matching_service = MatchService()

    def register_user(self, user: User) -> User:
        self._user[user.get_id()] = user
        return user

    def get_user(self, user_id: int) -> User:
        user = self._user.get(user_id)
        if not user:
            raise ValueError(f"user {user_id} not found")
        return user

    def get_matches(self):
        return self._matching_service.get_matches()

    def swipe(self, from_user_id: int, to_user_id: int, action: SwipeAction) -> Match | None:
        user1 = self.get_user(user_id=from_user_id)
        user2 = self.get_user(user_id=to_user_id)

        if not user1 or not user2:
            logger.error(f"User {from_user_id} or {to_user_id} not found")
            return None

        swipe = Swipe(user_id1=from_user_id, user_id2=to_user_id, action=action)
        user_pair = self._pair_key(user1.get_id(), user2.get_id())
        self._swipes[user_pair] = swipe
        if action is SwipeAction.LEFT:
            return None

        if user_pair in self._matches_by_pair:
            self._notification_service.send_notification(user1.get_id(),f"Match already exists for {user2.get_name()}")
            return None

        match_result = self._matcher.evaluate(user1, user2)
        if not match_result.passed:
            self._notification_service.send_notification(user1.get_id(),f"Match creation failed with {user2.get_name()} due to {', '.join(match_result.reasons)}")
            return None

        match = self._matching_service.create_match(user1.get_id(), user2.get_id())

        self._matches_by_pair[user_pair] = match.id
        user1.add_match(match.id)
        user2.add_match(match.id)
        self._notification_service.send_notification(user1.get_name(), f"Match found with {user2.get_name()}")
        self._notification_service.send_notification(user2.get_name(), f"Match found with {user1.get_name()}")
        return match

    @staticmethod
    def _pair_key(user1_id: int, user2_id: int) -> tuple[int, int]:
        return (user1_id, user2_id) if user1_id < user2_id else (user2_id, user1_id)
