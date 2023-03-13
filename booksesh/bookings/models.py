from django.db import models

from django.contrib.auth.models import User

from datetime import datetime


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
