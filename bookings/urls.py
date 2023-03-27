from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact),
    path('bookings.html', views.bookings, name='bookings'),
    path('submitbooking.html', views.submitbooking, name='submitbooking'),
    path('userview.html', views.userview, name='userview'),
    path('updatebooking/<int:id>', views.updatebooking, name='updatebooking'),
    path('submitupdatebooking/<int:id>', views.submitupdatebooking, name='submitupdatebooking'),
    path('staffview', views.staffview, name='staffview'),
    path('deletebooking/<int:id>', views.deletebooking, name='deletebooking'),
]

# NOT SURE WHAT THE DIFFERENCE IS BETWEEN BOTH URLS.PY FILES...
