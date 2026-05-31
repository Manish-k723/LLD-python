from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from Tinder2.enums import Gender
from Tinder2.user import User


@dataclass
class MatchResult:
    score: int = 0
    passed: bool = True
    reasons: list[str] = field(default_factory=list)


class MatchEvaluator(ABC):
    @abstractmethod
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        raise NotImplementedError


class BaseMatchEvaluator(MatchEvaluator):
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        return MatchResult()


class MatchDecorator(MatchEvaluator):
    def __init__(self, wrapped: MatchEvaluator):
        self._wrapped = wrapped

    def evaluate(self, user1: User, user2: User) -> MatchResult:
        return self._wrapped.evaluate(user1, user2)


class GenderMatchDecorator(MatchDecorator):
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        result = super().evaluate(user1, user2)
        if not result.passed:
            return result

        pref1 = user1.get_user_preferences().genders
        pref2 = user2.get_user_preferences().genders
        gender1 = user1.get_user_profile().get_gender()
        gender2 = user2.get_user_profile().get_gender()

        if pref1 and gender2 not in pref1:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user2.get_id()} gender not preferred by user {user1.get_id()}"])
        if pref2 and gender1 not in pref2:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user1.get_id()} gender not preferred by user {user2.get_id()}"])

        return MatchResult(score=result.score + 5, passed=True, reasons=result.reasons + ["gender compatibility passed (+5)"])


class AgeMatchDecorator(MatchDecorator):
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        result = super().evaluate(user1, user2)
        if not result.passed:
            return result

        age2 = user2.get_user_profile().get_age()
        age1 = user1.get_user_profile().get_age()
        pref1 = user1.get_user_preferences()
        pref2 = user2.get_user_preferences()

        if pref1.min_age is not None and age2 < pref1.min_age:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user2.get_id()} is below user {user1.get_id()} min age"])
        if pref1.max_age is not None and age2 > pref1.max_age:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user2.get_id()} is above user {user1.get_id()} max age"])
        if pref2.min_age is not None and age1 < pref2.min_age:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user1.get_id()} is below user {user2.get_id()} min age"])
        if pref2.max_age is not None and age1 > pref2.max_age:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"user {user1.get_id()} is above user {user2.get_id()} max age"])

        return MatchResult(score=result.score + 10, passed=True, reasons=result.reasons + ["age compatibility passed (+10)"])


class LocationMatchDecorator(MatchDecorator):
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        result = super().evaluate(user1, user2)
        if not result.passed:
            return result

        distance = user1.get_location().distance_to(user2.get_location())
        max_distance = min(
            user1.get_user_preferences().distance_km,
            user2.get_user_preferences().distance_km,
        )
        if distance > max_distance:
            return MatchResult(score=0, passed=False, reasons=result.reasons + [f"distance {distance:.2f} exceeds max {max_distance:.2f}"])

        return MatchResult(
            score=result.score + 15,
            passed=True,
            reasons=result.reasons + [f"location compatibility passed ({distance:.2f} km, +15)"],
        )


class InterestMatchDecorator(MatchDecorator):
    def evaluate(self, user1: User, user2: User) -> MatchResult:
        result = super().evaluate(user1, user2)
        if not result.passed:
            return result

        interests1 = {interest.name.lower() for interest in user1.get_user_profile().get_interests()}
        interests2 = {interest.name.lower() for interest in user2.get_user_profile().get_interests()}
        overlap = interests1 & interests2

        if not overlap:
            return MatchResult(score=0, passed=False, reasons=result.reasons + ["no shared interests"])

        bonus = 20
        return MatchResult(
            score=result.score + bonus,
            passed=True,
            reasons=result.reasons + [f"shared interests: {', '.join(sorted(overlap))} (+20)"],
        )


def build_matcher() -> MatchEvaluator:
    evaluator: MatchEvaluator = BaseMatchEvaluator()
    evaluator = InterestMatchDecorator(evaluator)
    evaluator = LocationMatchDecorator(evaluator)
    evaluator = AgeMatchDecorator(evaluator)
    evaluator = GenderMatchDecorator(evaluator)
    return evaluator
