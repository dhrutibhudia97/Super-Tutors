from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls), # not sure if this is meant to be here
    path('book-session', views.booksession, name='booksession'),
    path('session-submit', views.sessionsubmit, name='sessionsubmit'),
    path('user-View', views.userView, name='userView'),
    path('user-update-view/<int:id>', views.userUpdateView, name='userUpdateView'),
    path('session-update-submit/<int:id>', views.sessionUpdateSubmit, name='sessionUpdateSubmit'),
    path('staff-View', views.staffView, name='staffView'),
]

# NOT SURE WHAT THE DIFFERENCE IS BETWEEN BOTH URLS.PY FILES...
# NEED HELP CONNECTING HTML FILES IN TEMPLATE FOLDER...