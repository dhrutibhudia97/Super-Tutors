from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# same service 3 times, as up to 3 people can book the same group session
SERVICE_OPTIONS = (
    ("GCSE Biology", "GCSE Biology", "GCSE Biology"),
    ("GCSE Chemistry", "GCSE Chemistry", "GCSE Chemistry"),
    ("GCSE Physics", "GCSE Physics", "GCSE Physics"),
)

# 9 options for each time zone, so each group has max 3 people in it for 3 types of services
TIME_OPTIONS = (
    ("4-5pm", "4-5pm", "4-5pm", "4-5pm", "4-5pm", "4-5pm", "4-5pm", "4-5pm", "4-5pm"),
    ("5-6pm", "5-6pm", "5-6pm", "5-6pm", "5-6pm", "5-6pm", "5-6pm", "5-6pm", "5-6pm"),
    ("6-7pm", "6-7pm", "6-7pm", "6-7pm", "6-7pm", "6-7pm", "6-7pm", "6-7pm", "6-7pm"),
    ("7-8pm", "7-8pm", "7-8pm", "7-8pm", "7-8pm", "7-8pm", "7-8pm", "7-8pm", "7-8pm"),
    ("8-9pm", "8-9pm", "8-9pm", "8-9pm", "8-9pm", "8-9pm", "8-9pm", "8-9pm", "8-9pm"),
)

# Create your models here.


class Session(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    tutor_service = models.CharField(choices=SERVICE_OPTIONS)
    day = models.DateTimeField(default=datetime.now)
    time = models.CharField(choices=TIME_OPTIONS)
    ordered_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-day']

    def __str__(self):
        return f"Tutor Service: {self.tutor_service} | date: {self.day} | Time: {self.time}"
