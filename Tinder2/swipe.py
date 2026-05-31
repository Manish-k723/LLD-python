from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from Tinder2.enums import SwipeAction


@dataclass
class Swipe:
    id: int
    from_user_id: int
    to_user_id: int
    action: SwipeAction
    created_at: datetime

