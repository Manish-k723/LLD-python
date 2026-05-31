from __future__ import annotations

from dataclasses import dataclass, field

from Tinder2.enums import Gender


@dataclass
class Interest:
    name: str
    category: str


@dataclass
class UserPreference:
    min_age: int | None = None
    max_age: int | None = None
    distance_km: float = 5.0
    genders: list[Gender] = field(default_factory=list)
    interests: list[Interest] = field(default_factory=list)

