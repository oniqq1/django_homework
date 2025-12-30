from django.urls import path
from .views import sign_up , log_in
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("sign_up/", sign_up, name="sign_up"),
    path('',TemplateView.as_view(template_name='accounts/index.html'), name='index'),
    path("log_in/", log_in, name="log_in"),
    path("log_out/", LogoutView.as_view(next_page="index"), name="log_out")
]