from django.urls import path
from . import views

# Namespace for the profiles application URLs
app_name = "profiles"

# URL patterns for the profiles app
urlpatterns = [
    path(
        "", views.profiles_index, name="index"
    ),  # URL pattern for the profiles index page, showing all profiles
    path(
        "<str:username>/", views.profile, name="profile"
    ),  # URL pattern for an individual profile page, expects username as a string
]
