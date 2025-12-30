from django.urls import path
from .views import create_post , post, posts
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/', post, name='post'),
    path('', posts, name='posts'),
]