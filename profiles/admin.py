from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Profile model.

    This class customizes how Profile instances are displayed in the
    Django admin site.

    Attributes:
        list_display (tuple): Fields of the Profile model to display in the list view.
            - user: The associated User instance.
            - favorite_city: The user's favorite city.
    """

    list_display = ("user", "favorite_city")
