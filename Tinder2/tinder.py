from __future__ import annotations

from datetime import datetime

from Tinder2.chat import ChatService, Conversation, Message
from Tinder2.enums import SwipeAction
from Tinder2.match import Match
from Tinder2.matcher import MatchEvaluator, build_matcher
from Tinder2.notification import NotificationService
from Tinder2.swipe import Swipe
from Tinder2.user import User


class Tinder2:
    def __init__(self, matcher: MatchEvaluator | None = None):
        self._users: dict[int, User] = {}
        self._matches: dict[int, Match] = {}
        self._matches_by_pair: dict[tuple[int, int], int] = {}
        self._swipes: dict[tuple[int, int], Swipe] = {}
        self._next_match_id = 1
        self._next_swipe_id = 1
        self._matcher = matcher or build_matcher()
        self._notification_service = NotificationService()
        self._chat_service = ChatService()

    def register_user(self, user: User) -> User:
        self._users[user.get_id()] = user
        return user

    def get_user(self, user_id: int) -> User:
        user = self._users.get(user_id)
        if not user:
            raise ValueError(f"user {user_id} not found")
        return user

    def swipe(self, from_user_id: int, to_user_id: int, action: SwipeAction) -> Match | None:
        from_user = self.get_user(from_user_id)
        to_user = self.get_user(to_user_id)
        swipe = Swipe(
            id=self._next_swipe_id,
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            action=action,
            created_at=datetime.now(),
        )
        self._swipes[(from_user_id, to_user_id)] = swipe
        self._next_swipe_id += 1

        pair_key = self._pair_key(from_user_id, to_user_id)
        if pair_key in self._matches_by_pair:
            return self._matches[self._matches_by_pair[pair_key]]

        if action is SwipeAction.LEFT:
            return None

        reverse_swipe = self._swipes.get((to_user_id, from_user_id))
        if not reverse_swipe or reverse_swipe.action is not SwipeAction.RIGHT:
            return None

        result = self._matcher.evaluate(from_user, to_user)
        if not result.passed:
            self._notification_service.send_notification(
                from_user_id,
                f"No match with user {to_user_id}: {', '.join(result.reasons)}",
            )
            return None

        match = Match(
            id=self._next_match_id,
            user1_id=from_user_id,
            user2_id=to_user_id,
            matched_at=datetime.now(),
            score=result.score,
            reasons=result.reasons,
        )
        self._matches[self._next_match_id] = match
        self._matches_by_pair[pair_key] = self._next_match_id
        self._next_match_id += 1
        conversation = self._chat_service.open_conversation(match.id, match.user1_id, match.user2_id)

        from_user.add_match(match.id)
        to_user.add_match(match.id)
        self._notification_service.send_notification(from_user_id, f"Match found with user {to_user_id}")
        self._notification_service.send_notification(to_user_id, f"Match found with user {from_user_id}")
        self._notification_service.send_notification(match.user1_id, f"Conversation #{conversation.id} opened")
        self._notification_service.send_notification(match.user2_id, f"Conversation #{conversation.id} opened")
        return match

    def list_matches(self) -> list[Match]:
        return list(self._matches.values())

    def get_conversation(self, match_id: int) -> Conversation | None:
        return self._chat_service.get_conversation_by_match(match_id)

    def send_message(self, match_id: int, sender_id: int, text: str) -> Message:
        conversation = self._chat_service.get_conversation_by_match(match_id)
        if not conversation:
            raise ValueError(f"no conversation found for match {match_id}")
        message = self._chat_service.send_message(conversation.id, sender_id, text)
        recipient_id = conversation.user2_id if sender_id == conversation.user1_id else conversation.user1_id
        self._notification_service.send_notification(recipient_id, f"New message in conversation #{conversation.id}")
        return message

    def list_messages(self, match_id: int) -> list[Message]:
        conversation = self._chat_service.get_conversation_by_match(match_id)
        if not conversation:
            raise ValueError(f"no conversation found for match {match_id}")
        return self._chat_service.list_messages(conversation.id)

    def mark_messages_read(self, match_id: int, reader_id: int) -> None:
        conversation = self._chat_service.get_conversation_by_match(match_id)
        if not conversation:
            raise ValueError(f"no conversation found for match {match_id}")
        self._chat_service.mark_read(conversation.id, reader_id)

    @staticmethod
    def _pair_key(user1_id: int, user2_id: int) -> tuple[int, int]:
        return (user1_id, user2_id) if user1_id < user2_id else (user2_id, user1_id)
