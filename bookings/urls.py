from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact),
    # path('admin/', admin.site.urls), # not sure if this is meant to be here
    path('bookings.html', views.bookings, name='bookings'),
    path('submitbooking.html', views.submitbooking, name='submitbooking'),
#     path('session-submit', views.sessionsubmit, name='sessionsubmit'),
#     path('user-View', views.userView, name='userView'),
#     path('user-update-view/<int:id>', views.userUpdateView, name='userUpdateView'),
#     path('session-update-submit/<int:id>', views.sessionUpdateSubmit, name='sessionUpdateSubmit'),
#     path('staff-View', views.staffView, name='staffView'),
]

# NOT SURE WHAT THE DIFFERENCE IS BETWEEN BOTH URLS.PY FILES...
