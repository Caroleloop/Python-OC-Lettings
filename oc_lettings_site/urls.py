"""
URL configuration module for the 'oc_lettings_site' Django project.

This module defines the root URL patterns for the project, including
the admin site, the global homepage, and the included apps for lettings
and profiles. It also specifies custom error handlers.
"""

from django.contrib import admin
from django.urls import path, include
from . import views

# Root URL patterns for the project
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),  # Global homepage
    path(
        "lettings/", include("lettings.urls", namespace="lettings")
    ),  # Include the lettings app URLs
    path(
        "profiles/", include("profiles.urls", namespace="profiles")
    ),  # Include the profiles app URLs
]

# Custom error handlers
HANDLER404 = "oc_lettings_site.views.custom_404"  # Handler for 404 Page Not Found
HANDLER500 = "oc_lettings_site.views.custom_500"  # Handler for 500 Server Error
