"""bookingsessions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('summernote/', include('django_summernote.urls')),
    # path('', include('bookings.urls')),
    # path('', views.index, name='index'),
    # path('book-session', views.booksession, name='booksession'),
    # path('session-submit', views.sessionsubmit, name='sessionsubmit'),
    # path('user-View', views.userView, name='userView'),
    # path('user-update-view/<int:id>', views.userUpdateView, name='userUpdateView'),
    # path('session-update-submit/<int:id>', views.sessionUpdateSubmit, name='sessionUpdateSubmit'),
    # path('staff-View', views.staffView, name='staffView'),
]
