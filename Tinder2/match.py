from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Match:
    id: int
    user1_id: int
    user2_id: int
    matched_at: datetime
    score: int
    reasons: list[str]

