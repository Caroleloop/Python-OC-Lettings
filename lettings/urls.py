from django.urls import path
from . import views

# Namespace for the lettings application URLs
app_name = "lettings"

# URL patterns for the lettings app
urlpatterns = [
    path("", views.lettings_index, name="index"),
    # URL pattern for the lettings index page, showing all lettings
    path("<int:letting_id>/", views.letting, name="letting"),
    # URL pattern for an individual letting detail page, expects letting_id as an integer
]
