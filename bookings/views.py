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

    if request.method == 'POST':
        tuitiontype = request.POST.get('tuitiontype')
        day = request.POST.get('day')
        if tuitiontype == None:
            messages.success(request, "You need to select a tuition service first!")
            return redirect('bookings')

        #Store day and tuition type in django session:
        request.session['day'] = day
        request.session['tuitiontype'] = tuitiontype

        return redirect('bookingSubmit')


    return render(request, 'booksession.html', {
            'days':days,
            'validateDates':validateDates,
        })




def availableDates(days):
    today = datetime.now()
    days = []
    for i in range(0, days):
        futureDates = today + timedelta(days=i)
        d = futureDates.strftime('%A')
        if d == 'Monday' or d == 'Tuesday' or d == 'Wednesday' or d == 'Friday' or d == 'Saturday' or d == 'Sunday':
            days.append(futureDates.strftime('%d-%m-%y'))
    return days


def isDateValid(futureDates):
    validateDates = []
    for a in futureDates:
        if bookingsessions().objects.filter(day=a).count() < 13:
            validateDates.append(a)
    return validateDates
