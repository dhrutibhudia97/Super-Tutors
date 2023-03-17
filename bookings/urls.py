from . import views
from django.urls import path


urlpatterns = [
    path('theblog.html', views.PostList.as_view(), name='blog')
]