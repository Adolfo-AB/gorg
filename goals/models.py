from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
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
    timespan = models.CharField(choices=TIMESPAN_CHOICES, default=DAILY, max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
