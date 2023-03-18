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

        # Store day and tuition type in django session:
        request.session['day'] = day
        request.session['tuitiontype'] = tuitiontype

        return redirect('submitBooking')

    return render(request, 'booksession.html', {
            'days': days,
            'validateDates': validateDates,
        })


def submitBooking(request):
    user = request.user.username
    times = ["4-5 PM", "5-6 PM", "6-7 PM", "7-8 PM", "8-9 PM"]
    today - datetime.now()
    earliestDate = today.strftime('%d-%m-%y')
    timerange = today + timedelta(days=14)
    strtimerange = timerange.strftime('%d=%m-%y')
    latestDate = strtimerange

    day = request.session.get('day')
    tuitiontype = request.session.get('tuitiontype')

    timeslot = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = strDay(day)

        if tuitiontype != None:
            if day <= latestDate and day >= earliestDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if bookingsessions.objects.filter(day=day).count() < 6:
                        if bookingsessions.objects.filter(day=day, time=time).count() < 1:
                            bookingSessionStatus = bookingsessions.objects.get_or_create(
                                user=user,
                                tuitiontype=tuitiontype,
                                day=day, 
                                time=time,
                            )
                            messages.success(request, "Tuition session has been booked.")
                            return redirect('index')
                        else:
                            messages.success(request, "This time is not available.")
                    else:
                        messages.success(request, "This day is fully booked")
                else:
                    messages.success(request, "Tuition cannot be booked on this day right now")
            else:
                messages.success(request, "Tuition cannot be booked on this day right now")
        else:
            messages.success(request, "You need to select a tuition type.")
        
    return render(request, 'sessionsubmit.html', {
        'times': timeslot,
    })


def userView(request):
    user = request.user
    sessionsBooked = bookingsessions.objects.filter(user=user).order_by('day', 'time')
    return render(request, "userView.html", {
        'user': user,
        'sessionsBooked': sessionsBooked,
    })


def updateBooking(request, id):
    bookingsessions = bookingsessions.object.get(pk=id)
    bookedDate = bookingsessions.day

    today = datetime.today()
    earliestDate = today.strftime('%d-%m-%y')

    withinTwoDays = (bookedDate).strftime('%d-%m-%y') >= (today + timedelta(days=2)).strftime('%d=%m-%y')
    days = availableDates(15)

    validateDates = isDateValid(days)


    if request.method == 'POST':
        tuitiontype = request.POST.get('tuitiontype')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['tuitiontype'] = tuitiontype

        return redirect('submitUpdateBooking', id=id)
    

    return render(request, 'userUpdateView.html', {
        'days': days,
        'validateDates': validateDates,
        'withinTwoDays': withinTwoDays,
        'id': id,
    })


def submitUpdateBooking(request, id):
    user = request.user.username
    times = ["4-5 PM", "5-6 PM", "6-7 PM", "7-8 PM", "8-9 PM"]
    today - datetime.now()
    earliestDate = today.strftime('%d-%m-%y')
    timerange = today + timedelta(days=14)
    strtimerange = timerange.strftime('%d=%m-%y')
    latestDate = strtimerange

    day = request.session.get('day')
    tuitiontype = request.session.get('tuitiontype')

    timeslot = checkEditTime(times, day, id)
    bookingsessions = bookingsessions.objects.get(pk=id)
    userBookedTime = bookingsessions.time 
    if request.method == 'POST':
        time = request.POST.get("time")
        date = strDay(day)

        if tuitiontype != None:
            if day <= latestDate and day >= earliestDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if bookingsessions.objects.filter(day=day).count() < 6:
                        if bookingsessions.objects.filter(day=day, time=time).count() < 1 or userBookedTime == time:
                            bookingSessionStatus = bookingsessions.objects.filter(pk=id).update(
                                user=user,
                                tuitiontype=tuitiontype,
                                day=day, 
                                time=time,
                            )
                            messages.success(request, "Tuition session has been successfully changed!")
                            return redirect('index')
                        else:
                            messages.success(request, "This time has already been booked by someone else.")
                    else:
                        messages.success(request, "This day is fully booked")
                else:
                    messages.success(request, "Tuition cannot be booked on this day right now")
            else:
                messages.success(request, "Tuition cannot be booked on this day right now")
        else:
            messages.success(request, "You need to select a tuition type.")
        return redirect('userView')
        
    return render(request, 'sessionUpdateSubmit.html', {
        'times': timeslot,
        'id': id,
    })


def staffView(request):
    today = datetime.today()
    earliestDate = today.strftime('%d-%m-%y')
    timerange = today + timedelta(days=15)
    strtimerange = timerange.strftime('%d-%m-%y')
    latestDate = strtimerange

    bookedSessions = bookingsessions.objects.filter(day_range=[earliestDate, latestDate]).order_by('day', 'time')

    return render(request, 'staffView.html', {
        'bookedSessions': bookedSessions,
    })



     
def stringDay(futureDates):
    t = datetime.strftime(futureDates, '%d-%m-%y')
    d = t.strftime('%A')
    return d
    

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


def checkTime(times, day):
    futureDates = []
    for o in times:
        if bookingsessions.objects.filter(day=day, time=o).count() < 1:
            futureDates.append(o)
    return futureDates