from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from datetime import datetime


# STATUS = ((0, "Draft"), (1, "Published"))

TUITION_CHOICES = (
    ("GCSE Biology", "GCSE Biology"), ("GCSE Chemistry", "GCSE Chemistry"), ("GCSE Physics", "GCSE Physics"),
    ("A-LEVEL Biology", "A-LEVEL Biology"), ("A-LEVEL Chemistry", "A-LEVEL Chemistry"), ("A-LEVEL Physics", "A-LEVEL Physics")
)

TIME_CHOICES = (
    ("4-5 PM", "4-5 PM"), ("5-6 PM", "5-6 PM"), ("6-7 PM", "6-7 PM"), ("7-8 PM", "7-8 PM"), ("8-9 PM", "8-9 PM")
)
# Create your models here.


class bookingsession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, blank=False)
    tuitiontype = models.CharField(max_length=75, choices=TUITION_CHOICES, default="GCSE Biology")
    day = models.DateField(datetime.now)
    time_choice = models.CharField(max_length=6, choices=TIME_CHOICES, default="4-5 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time_choice}"


