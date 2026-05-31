from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"


class SwipeAction(Enum):
    LEFT = "left"
    RIGHT = "right"


class MatchStatus(Enum):
    MATCHED = "matched"
    NOT_MATCHED = "not_matched"

