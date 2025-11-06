from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),  # page d'accueil globale
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]

HANDLER404 = "oc_lettings_site.views.custom_404"
HANDLER500 = "oc_lettings_site.views.custom_500"
