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
    path('deletebooking/<int:id>', views.deletebooking, name='deletebooking'),
]
