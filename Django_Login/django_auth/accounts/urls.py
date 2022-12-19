from django.urls import path
from .views import dashboard, profile_list, profile, register
from django.conf.urls import include


app_name = "System_Post"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/register/", register, name="register"),
]