from django.contrib import admin
# from .models import Post
from .models import *
from django_summernote.admin import SummernoteModelAdmin # might need to comment out

admin.site.register(bookingsession)

