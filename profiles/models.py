from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (OneToOneField): One-to-one relationship with the Django User model.
            - on_delete=models.CASCADE ensures that the profile is deleted if the user is deleted.
            - related_name='profile_new' allows reverse access from the User instance.
        favorite_city (CharField): Optional field storing the user's favorite city
            (max length 64 characters, can be blank).
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile_new"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a human-readable string representation of the Profile.

        Returns:
            str: The username of the associated User.
        """
        return self.user.username
