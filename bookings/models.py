from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from datetime import datetime


# STATUS = ((0, "Draft"), (1, "Published"))

TUITION_CHOICES = (
    ("GCSE Biology", "GCSE Biology"), ("GCSE Chemistry", "GCSE Chemistry"), ("GCSE Physics", "GCSE Physics"),
    ("A-LEVEL Biology", "A-Level Biology"), ("A-LEVEL Chemistry", "A-LEVEL Chemistry"), ("A-LEVEL Physics", "A-LEVEL Physics")
)

TIME_CHOICES = (
    ("4-5 PM", "4-5 PM"), ("5-6 PM", "5-6 PM"), ("6-7 PM", "6-7 PM"), ("7-8 PM", "7-8 PM"), ("8-9 PM", "8-9 PM")
)
# Create your models here.


class bookingsessions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, blank=False)
    tuitiontype = models.CharField(max_length=75, choices=TUITION_CHOICES, default="GCSE Biology")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=6, choices=TIME_CHOICES, default="4 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

# class Post(models.Model):
#     title = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     featured_image = CloudinaryField('image', default='placeholder')
#     excerpt = models.TextField(blank=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

#     class Meta:
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.title

    # def number_of_likes(self):
    #     return self.likes.count()

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"
