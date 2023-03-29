from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from datetime import datetime, timedelta


def index(request):
    return render(request, "index.html", {})


def contact(request):
    return render(request, "contact.html", {})


def bookings(request):
    days = availableDate(15)
    validateDates = isDateValid(days)

    if request.method == 'POST':
        tuitiontype = request.POST.get('tuitiontype')
        day = request.POST.get('day')
        if tuitiontype is None:
            messages.error(request, "You need to select a tuition service first!")
            return redirect('bookings')

        request.session['day'] = day
        request.session['tuitiontype'] = tuitiontype

        return redirect('submitbooking.html')

    print(days)
    return render(request, 'bookings.html', {
        'days': days,
        'validateDates': validateDates,
        })


def submitbooking(request):
    user = request.user
    times = ["4-5 PM", "5-6 PM", "6-7 PM", "7-8 PM", "8-9 PM"]
    today = datetime.today()
    earliestDate = today.strftime('%Y-%m-%d')
    timerange = today + timedelta(days=14)
    strtimerange = timerange.strftime('%Y-%m-%d')
    latestDate = strtimerange

    day = request.session.get('day')
    tuitiontype = request.session.get('tuitiontype')

    timeslot = checkTime(times, day)
    if request.method == 'POST':
        time_choice = request.POST.get("time_choice")
        date = stringDay(day)

        if tuitiontype != None:
            if day <= latestDate and day >= earliestDate:
                if date != 'Thursday':
                    if Bookingtuition.objects.filter(day=day).count() < 13:
                        if Bookingtuition.objects.filter(day=day, time_choice=time_choice).count() < 1:
                            bookingSessionStatus = Bookingtuition.objects.get_or_create(
                                user = user,
                                tuitiontype = tuitiontype,
                                day = day, 
                                time_choice = time_choice,
                            )
                            messages.success(request, "Tuition session booked.")
                            return redirect('userview')
                        else:
                            messages.error(request, "This time is not available.")
                    else:
                        messages.error(request, "This day is fully booked")
                else:
                    messages.error(request, "We are not open on Thursdays!")
            else:
                messages.error(request, "Tuition cannot be booked more than two weeks in advance")
        else:
            messages.error(request, "You need to select a tuition type.")
        
    return render(request, 'submitbooking.html', {
        'times': timeslot,
    })


def userview(request):
    user = request.user
    sessionsbooked = Bookingtuition.objects.filter(user=user).order_by('day', 'time_choice')
    return render(request, "userview.html", {
        'user': user,
        'sessionsbooked': sessionsbooked,
    })


def deletebooking(request, id):
    bookingtuition = Bookingtuition.objects.get(pk=id)
    bookingtuition.delete()
    messages.success(request, "Tuition session was deleted.")
    return redirect('userview')


def updatebooking(request, id):
    bookingtuition = Bookingtuition.objects.get(pk=id)
    bookedDate = bookingtuition.day

    today = datetime.today()
    earliestDate = today.strftime('%Y-%m-%d')

    withinTwoDays = (bookedDate).strftime('%Y-%m-%d') >= (today + timedelta(days=2)).strftime('%Y-%m-%d')
    days = availableDate(15)

    validateDates = isDateValid(days)

    if request.method == 'POST':
        tuitiontype = request.POST.get('tuitiontype')
        day = request.POST.get('day')
        request.session['day'] = day
        request.session['tuitiontype'] = tuitiontype

        return redirect('submitupdatebooking', id=id)
    
    return render(request, 'updatebooking.html', {
        'days': days,
        'validateDates': validateDates,
        'withinTwoDays': withinTwoDays,
        'id': id,
    })


def submitupdatebooking(request, id):
    user = request.user
    times = ["4-5 PM", "5-6 PM", "6-7 PM", "7-8 PM", "8-9 PM"]
    today = datetime.today()
    earliestDate = today.strftime('%Y-%m-%d')
    timerange = today + timedelta(days=14)
    strtimerange = timerange.strftime('%Y-%m-%d')
    latestDate = strtimerange

    day = request.session.get('day')
    tuitiontype = request.session.get('tuitiontype')

    timeslot = checkEditTime(times, day, id)
    bookingtuition = Bookingtuition.objects.get(pk=id)
    userBookedTime = bookingtuition.time_choice
    if request.method == 'POST':
        time_choice = request.POST.get("time_choice")
        date = stringDay(day)
        print(tuitiontype, day, time_choice)
        if tuitiontype != None:
            if day <= latestDate and day >= earliestDate:
                if date != 'Thursday':
                    if Bookingtuition.objects.filter(day=day).count() < 6:
                        if Bookingtuition.objects.filter(day=day, time_choice=time_choice).count() < 1 or userBookedTime == time_choice:
                            bookingSessionStatus = Bookingtuition.objects.filter(pk=id).update(
                                user=user,
                                tuitiontype=tuitiontype,
                                day=day, 
                                time_choice=time_choice,
                            )
                            messages.success(request, "Tuition session has been successfully changed!")
                            return redirect('userview')
                        else:
                            messages.error(request, "This time has already been booked by someone else.")
                    else:
                        messages.error(request, "This day is fully booked")
                else:
                    messages.error(request, "Tuition cannot be booked on this day right now")
            else:
                messages.error(request, "Tuition cannot be booked on this day right now")
        else:
            messages.error(request, "You need to select a tuition type.")
        return redirect('userview')
        
    return render(request, 'submitupdatebooking.html', {
        'times': timeslot,
        'id': id,
    })

     
def stringDay(futureDates):
    t = datetime.strptime(futureDates, '%Y-%m-%d')
    d = t.strftime('%A')
    return d


def availableDate(days):
    today = datetime.now()
    days = []
    for i in range(0, 15):
        day = today + timedelta(days=i)
        if day.weekday() != 'Thursday':
            days.append(day.strftime('%Y-%m-%d'))
    return days


def isDateValid(futureDates):
    validateDates = []
    for a in futureDates:
        if Bookingtuition.objects.filter(day=a).count() < 13:
            validateDates.append(a)
    return validateDates


def checkTime(times, day):
    futureDates = []
    for o in times:
        if Bookingtuition.objects.filter(day=day, time_choice=o).count() < 1:
            futureDates.append(o)
    return futureDates


def checkEditTime(times, day, id):
    futureDates = []
    bookingtuition = Bookingtuition.objects.get(pk=id)
    time_choice = bookingtuition.time_choice
    for o in times:
        if Bookingtuition.objects.filter(day=day, time_choice=o).count() < 1 or time_choice == o:
            futureDates.append(o)
    return futureDates
