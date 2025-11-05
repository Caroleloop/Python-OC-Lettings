from django.urls import path
from . import views

app_name = "profiles"  # espace de nom

urlpatterns = [
    path("", views.profiles_index, name="index"),  # index des profils
    path("<str:username>/", views.profile, name="profile"),
]
