from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Conversation:
    id: int
    match_id: int
    user1_id: int
    user2_id: int
    created_at: datetime
    status: str = "active"


@dataclass
class Message:
    id: int
    conversation_id: int
    sender_id: int
    text: str
    sent_at: datetime
    read_at: datetime | None = None


class ChatService:
    def __init__(self) -> None:
        self._conversations: dict[int, Conversation] = {}
        self._conversation_by_match: dict[int, int] = {}
        self._messages_by_conversation: dict[int, list[Message]] = {}
        self._next_conversation_id = 1
        self._next_message_id = 1

    def open_conversation(self, match_id: int, user1_id: int, user2_id: int) -> Conversation:
        conversation_id = self._conversation_by_match.get(match_id)
        if conversation_id is not None:
            return self._conversations[conversation_id]

        conversation = Conversation(
            id=self._next_conversation_id,
            match_id=match_id,
            user1_id=user1_id,
            user2_id=user2_id,
            created_at=datetime.now(),
        )
        self._conversations[conversation.id] = conversation
        self._conversation_by_match[match_id] = conversation.id
        self._messages_by_conversation[conversation.id] = []
        self._next_conversation_id += 1
        return conversation

    def get_conversation_by_match(self, match_id: int) -> Conversation | None:
        conversation_id = self._conversation_by_match.get(match_id)
        if conversation_id is None:
            return None
        return self._conversations[conversation_id]

    def send_message(self, conversation_id: int, sender_id: int, text: str) -> Message:
        conversation = self._conversations.get(conversation_id)
        if not conversation:
            raise ValueError(f"conversation {conversation_id} not found")
        if sender_id not in (conversation.user1_id, conversation.user2_id):
            raise ValueError(f"user {sender_id} is not part of conversation {conversation_id}")
        if conversation.status != "active":
            raise ValueError(f"conversation {conversation_id} is not active")

        message = Message(
            id=self._next_message_id,
            conversation_id=conversation_id,
            sender_id=sender_id,
            text=text,
            sent_at=datetime.now(),
        )
        self._messages_by_conversation[conversation_id].append(message)
        self._next_message_id += 1
        return message

    def list_messages(self, conversation_id: int) -> list[Message]:
        if conversation_id not in self._conversations:
            raise ValueError(f"conversation {conversation_id} not found")
        return list(self._messages_by_conversation.get(conversation_id, []))

    def mark_read(self, conversation_id: int, reader_id: int) -> None:
        conversation = self._conversations.get(conversation_id)
        if not conversation:
            raise ValueError(f"conversation {conversation_id} not found")
        if reader_id not in (conversation.user1_id, conversation.user2_id):
            raise ValueError(f"user {reader_id} is not part of conversation {conversation_id}")

        now = datetime.now()
        for message in self._messages_by_conversation.get(conversation_id, []):
            if message.sender_id != reader_id and message.read_at is None:
                message.read_at = now

