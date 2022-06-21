from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timedelta


class Goal(models.Model):
    class Timespan:
        DAILY = "DA"
        WEEKLY = "WE"
        MONTHLY = "MO"
        YEARLY = "YE"
        TIMESPAN_CHOICES = [
            (DAILY, "Daily"),
            (WEEKLY, "Weekly"),
            (MONTHLY, "Monthly"),
            (YEARLY, "Yearly"),
        ]

    class Status:
        IN_PROGRESS = "IP"
        COMPLETED = "CO"
        UNFINISHED = "UN"
        STATUS_CHOICES = [
            (IN_PROGRESS, "In Progress"),
            (COMPLETED, "Completed"),
            (UNFINISHED, "Unfinished"),
        ]


    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, default="")
    timespan = models.CharField(choices=Timespan.TIMESPAN_CHOICES, default=Timespan.DAILY, max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(auto_now_add=False)
    status = models.CharField(choices=Status.STATUS_CHOICES, default=Status.IN_PROGRESS, max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")

    def save(self, *args, **kwargs):
        if self.timespan == self.Timespan.DAILY:
            self.expiry = (self.created + timedelta(days=1)).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.WEEKLY:
            self.expiry = (self.created + + timedelta((-1-self.created.weekday())%7+1)).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.MONTHLY:
            self.expiry = (self.created.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.YEARLY:
            self.expiry = datetime(year=self.created.year+1, month=1, day=1)

        super(Goal, self).save(*args, **kwargs)