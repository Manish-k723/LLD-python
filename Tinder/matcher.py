from dataclasses import field
from abc import ABC, abstractmethod
from dataclasses import dataclass
from Tinder.user import User

@dataclass
class MatchScore:
    score: int = 0
    passed: bool = True
    reasons: list[str] = field(default_factory=list)

class MatchEvaluator(ABC):
    @abstractmethod
    def evaluate(self, user1, user2):
        raise NotImplementedError

class BaseMatchEvaluator(MatchEvaluator):
    def evaluate(self, user1, user2):
        return MatchScore()

class MatchDecorator(MatchEvaluator):
    def __init__(self, wrapped: MatchEvaluator = None):
        self._wrapper = wrapped

    def evaluate(self, user1: User, user2: User):
        return self._wrapper.evaluate(user1, user2)

class GenderMatchEvaluator(MatchDecorator):
    def evaluate(self, user1, user2):
        result = super().evaluate(user1, user2)

        if not result.passed:
            return result

        g1 = user1.get_user_profile().get_gender()
        g2 = user2.get_user_profile().get_gender()

        g1_interest = user1.get_user_preferences().get_gender()
        g2_interest = user2.get_user_preferences().get_gender()

        if g1 not in g2_interest:
            return MatchScore(score = 0, passed = False, reasons = result.reasons + [f"user {user1.get_id()} gender not preferred by user {user2.get_id()}"])
        if g2 not in g1_interest:
            return MatchScore(score = 0, passed = False, reasons = result.reasons + [f"user {user2.get_id()} gender not preferred by user {user1.get_id()}"])

        return MatchScore(score = result.score + 50, passed = True, reasons = result.reasons + ["gender compatibility passed (+5)"])


class AgeMatchEvaluator(MatchDecorator):
    def evaluate(self, user1, user2):
        result = super().evaluate(user1, user2)

        if not result.passed:
            return result

        age2 = user2.get_user_profile().get_age()
        age1 = user1.get_user_profile().get_age()
        pref1 = user1.get_user_preferences()
        pref2 = user2.get_user_preferences()

        if pref1.get_min_age() is not None and age2 < pref1.get_min_age():
            return MatchScore(score=0, passed=False, reasons=result.reasons + [
                f"user {user2.get_id()} is below user {user1.get_id()} min age"])
        if pref1.get_max_age() is not None and age2 > pref1.get_max_age():
            return MatchScore(score=0, passed=False, reasons=result.reasons + [
                f"user {user2.get_id()} is above user {user1.get_id()} max age"])
        if pref2.get_min_age() is not None and age1 < pref2.get_min_age():
            return MatchScore(score=0, passed=False, reasons=result.reasons + [
                f"user {user1.get_id()} is below user {user2.get_id()} min age"])
        if pref2.get_max_age() is not None and age1 > pref2.get_max_age():
            return MatchScore(score=0, passed=False, reasons=result.reasons + [
                f"user {user1.get_id()} is above user {user2.get_id()} max age"])

        return MatchScore(score=result.score + 50, passed=True,
                           reasons=result.reasons + ["age compatibility passed (+10)"])

def build_matcher() -> MatchEvaluator:
    evaluate: MatchEvaluator = BaseMatchEvaluator()
    evaluate = GenderMatchEvaluator(evaluate)
    evaluate = AgeMatchEvaluator(evaluate)
    return evaluate

