from enum import Enum
from typing import List


class RecurrencePattern:
    class Type(Enum):
        Daily = "daily"  # e.g. Repeat event every 3 days.
        Weekly = "weekly"  # e.g. Repeat event Monday and Tuesday of every other week.
        AbsoluteMonthly = "absoluteMonthly"  # e.g. Repeat event quarterly (every 3 months) on the 15th.
        RelativeMonthly = "relativeMonthly"  # e.g. Repeat event on the second Thursday or Friday every three months.
        AbsoluteYearly = (
            "absoluteYearly"  # e.g. Repeat event on the 15th of March every 3 years.
        )
        RelativeYearly = "relativeYearly"  # e.g. Repeat event on the second Thursday or Friday of every November every 3 years.

    class DayOfWeek:
        Sunday = "sunday"
        Monday = "monday"
        Tuesday = "tuesday"
        Wednesday = "wednesday"
        Thursday = "thursday"
        Friday = "friday"
        Saturday = "saturday"

    def __init__(self):
        self.body = {}

    def __setitem__(self, key, value):
        self.body[key] = value

    @classmethod
    def daily(cls, interval: int):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.Daily)
        recurrence.set_interval(interval)
        return recurrence.body

    @classmethod
    def weekly(cls, interval: int, days_of_week: List[DayOfWeek], first_day_of_week: DayOfWeek):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.Weekly)
        recurrence.set_interval(interval)
        recurrence.set_days_of_week(days_of_week)
        recurrence.set_first_day_of_week(first_day_of_week)
        return recurrence.body

    @classmethod
    def absolute_monthly(cls, interval: int, day_of_month: int):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.AbsoluteMonthly)
        recurrence.set_interval(interval)
        recurrence.set_day_of_month(day_of_month)
        return recurrence.body

    @classmethod
    def relative_monthly(cls, interval: int, days_of_week: List[DayOfWeek]):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.RelativeMonthly)
        recurrence.set_interval(interval)
        recurrence.set_days_of_week(days_of_week)
        return recurrence.body

    @classmethod
    def absolute_yearly(cls, interval: int, day_of_month: int, month: int):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.AbsoluteYearly)
        recurrence.set_interval(interval)
        recurrence.set_day_of_month(day_of_month)
        recurrence.set_month(month)
        return recurrence.body

    @classmethod
    def relative_yearly(cls, interval: int, days_of_week: List[DayOfWeek], month: int):
        recurrence = cls()
        recurrence.set_pattern_type(cls.Type.AbsoluteYearly)
        recurrence.set_interval(interval)
        recurrence.set_days_of_week(days_of_week)
        recurrence.set_month(month)
        return recurrence.body

    def set_pattern_type(self, pattern: Type):
        self["type"] = pattern.value

    def set_interval(self, interval: int):
        self["interval"] = interval

    def set_days_of_week(self, days_of_week: List[DayOfWeek]):
        self["daysOfWeek"] = days_of_week

    def set_first_day_of_week(self, first_day_of_week: DayOfWeek):
        self["firstDayOfWeek"] = first_day_of_week

    def set_day_of_month(self, day_of_month: int):
        self["dayOfMonth"] = day_of_month

    def set_month(self, month):
        assert 0 < month < 12
        self["month"] = month