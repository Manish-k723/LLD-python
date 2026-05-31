from abc import ABC, abstractmethod
from enums import RecurringFrequency

class RecurringRule(ABC):
    def __init__(self, interval: int, end_date: str):
        self._interval = interval
        self._end_date = end_date

    @abstractmethod
    def expand(self):
        raise NotImplementedError("Subclasses must implement this method")


class WeeklyRecurringRule(RecurringRule):
    def expand(self):
        return self._interval * 7

class MonthlyRecurringRule(RecurringRule):
    def expand(self):
        return self._interval * 30

class DailyRecurringRule(RecurringRule):
    def expand(self):
        return self._interval


class RecurringRuleFactory:
    @staticmethod
    def create_rule(frequency, interval, end_date):
        if frequency == RecurringFrequency.DAILY:
            return DailyRecurringRule(interval, end_date)
        elif frequency == RecurringFrequency.WEEKLY:
            return WeeklyRecurringRule(interval, end_date)
        elif frequency == RecurringFrequency.MONTHLY:
            return MonthlyRecurringRule(interval, end_date)
        else:
            raise ValueError(f"Unsupported recurrence frequency: {frequency}")