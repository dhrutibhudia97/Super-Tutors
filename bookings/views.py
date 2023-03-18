from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
# from .models import Post
from .models import *
from datetime import datetime, timedelta


# Create your views here.

# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by('-created-on')
#     template_name = 'theblog.html'
#     paginate_by = 8


def index(request):
    return render(request, "index.html", {})

def bookings(request):
    days = availableDates(15)
    validateDates = isDateValid(dates)


def availableDates(days):
    today = datetime.now()
    days = []
    for i in range (0, days):
        futureDates = today + timedelta(days=i)
        d = futureDates.strftime('%A')
        if d == 'Monday' or d == 'Tuesday' or d == 'Wednesday' or d == 'Friday' or d == 'Saturday' or d == 'Sunday':
            days.append(futureDates.strftime('%d-%m-%Y'))
    return days
