from django.contrib import admin
from django.urls import path, include
from . import views
from .views_sentry_test import trigger_404, trigger_500


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
    path("test-404/", trigger_404),
    path("test-500/", trigger_500),
]


# Custom error handlers
handler404 = "oc_lettings_site.views.custom_404"  # Handler for 404 Page Not Found
handler500 = "oc_lettings_site.views.custom_500"  # Handler for 500 Server Error
