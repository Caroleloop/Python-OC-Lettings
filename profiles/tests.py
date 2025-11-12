from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from unittest.mock import patch


# =======================
# TESTS DU MODELE
# =======================
class ProfileModelTest(TestCase):
    """
    Test case for the Profile model.

    Verifies that the model fields and string representation work as expected.
    """

    def setUp(self):
        """Create a sample User and Profile instance for testing."""
        self.user = User.objects.create_user(username="john", password="testpass")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_str(self):
        """Test that the string representation of Profile returns the username."""
        self.assertEqual(str(self.profile), "john")

    def test_favorite_city_field(self):
        """Test that the favorite_city field is correctly assigned."""
        self.assertEqual(self.profile.favorite_city, "Paris")


# =======================
# TESTS DES VUES ET URLS
# =======================
class ProfilesViewsTest(TestCase):
    """
    Integration tests for profiles views and URLs.

    Verifies that the index and profile detail pages render correctly
    and display the expected content.
    """

    def setUp(self):
        """Create a test client, a User, and associated Profile for testing."""
        self.client = Client()
        self.user = User.objects.create_user(username="jane", password="12345")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Lyon")

    def test_profiles_index_view(self):
        """
        Test that the profiles index view returns HTTP 200,
        uses the correct template, and displays the usernames.
        """
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, "jane")

    def test_profile_detail_view(self):
        """
        Test that the profile detail view returns HTTP 200,
        uses the correct template, and displays profile information.
        """
        url = reverse("profiles:profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "jane")
        self.assertContains(response, "Lyon")

    def test_profile_detail_view_not_found(self):
        """
        Test that accessing a non-existing profile raises Profile.DoesNotExist.
        """
        with patch(
            "profiles.views.Profile.objects.all", side_effect=Exception("DB error")
        ):
            url = reverse("profiles:index")
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "profiles/index.html")
            self.assertIn("profiles_list", response.context)
            self.assertEqual(list(response.context["profiles_list"]), [])
