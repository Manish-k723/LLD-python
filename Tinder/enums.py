from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class MatchStatus(Enum):
    MATCHED = "matched"
    NOT_MATCHED = "not_matched"

class SwipeAction(Enum):
    LEFT = "left"
    RIGHT = "right"

class MatchType(Enum):
    AGE = "age"
    BASIC = "basic"
    LOCATION = "location"
    INTERESTS = "interest"