from datetime import datetime
from enum import Enum

from todocli.todo_api.todo_api_util import api_timestamp_to_datetime


class Task:
    class Status(Enum):
        Completed = "completed"
        NotStarted = "notStarted"
        InProgress = "inProgress"
        WaitingOnOthers = "waitingOnOthers"
        Deferred = "deferred"

    class Importance(Enum):
        Low = "low"
        Normal = "normal"
        High = "high"

    class RecurrencePattern(Enum):
        Daily = "daily"                     # e.g. Repeat event every 3 days.
        Weekly = "weekly"                   # e.g. Repeat event Monday and Tuesday of every other week.
        AbsoluteMonthly = "absoluteMonthly" # e.g. Repeat event quarterly (every 3 months) on the 15th.
        RelativeMonthly = "relativeMonthly" # e.g. Repeat event on the second Thursday or Friday every three months.
        AbsoluteYearly = "absoluteYearly"   # e.g. Repeat event on the 15th of March every 3 years.
        RelativeYearly = "relativeYearly"   # e.g. Repeat event on the second Thursday or Friday of every November every 3 years.

    def __init__(self, query_result):
        self.title = query_result["title"]
        self.id = query_result["id"]
        self.importance = Task.Importance(query_result["importance"])
        self.status = Task.Status(query_result["status"])
        self.created_datetime = api_timestamp_to_datetime(
            query_result["createdDateTime"]
        )

        if "completedDateTime" in query_result:
            self.completed_datetime = api_timestamp_to_datetime(
                query_result["completedDateTime"]
            )
        else:
            self.completed_datetime = None

        self.is_reminder_on: bool = bool(query_result["isReminderOn"])

        if "reminderDateTime" in query_result:
            self.reminder_datetime = api_timestamp_to_datetime(
                query_result["reminderDateTime"]
            )
        else:
            self.reminder_datetime = None

        self.last_modified_datetime = api_timestamp_to_datetime(
            query_result["lastModifiedDateTime"]
        )

        if "bodyLastModifiedDateTime" in query_result:
            self.body_last_modified_datetime = api_timestamp_to_datetime(
                query_result["bodyLastModifiedDateTime"]
            )
        else:
            self.body_last_modified_datetime = None
