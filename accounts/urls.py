from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *
from . import views


urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/update/", profile_edit, name="profile_edit"),
    path('about/', views.about_view, name='about'),
]