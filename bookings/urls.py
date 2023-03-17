from . import views
from django.urls import path


urlpatterns = [
    path('blog.html', views.PostList.as_view(), name='blog')
]