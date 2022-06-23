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

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, default="")
    timespan = models.CharField(choices=Timespan.TIMESPAN_CHOICES, default=Timespan.DAILY, max_length=2)
    created = models.DateTimeField(default=None, blank=True, null=True)
    expiry = models.DateTimeField(default=None, blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.created = now

        if self.timespan == self.Timespan.DAILY:
            self.expiry = (now + timedelta(days=1)).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.WEEKLY:
            self.expiry = (now + + timedelta((-1-self.created.weekday())%7+1)).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.MONTHLY:
            self.expiry = (now.replace(day=1) + timedelta(days=32)).replace(day=1).replace(hour=00, minute=00, second=00, microsecond=00)
        if self.timespan == self.Timespan.YEARLY:
            self.expiry = datetime(year=now.year+1, month=1, day=1)

        super(Goal, self).save(*args, **kwargs)

    @property
    def is_expired(self):
        if datetime.now > self.expiry:
            return True
        return False