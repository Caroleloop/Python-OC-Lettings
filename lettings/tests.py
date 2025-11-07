from django.test import TestCase, Client
from django.urls import reverse
from .models import Address, Letting


# =======================
# TESTS DES MODÈLES
# =======================
class AddressModelTest(TestCase):
    """
    Test case for the Address model.

    Verifies field assignments and string representation.
    """

    def setUp(self):
        """Create a sample Address instance for testing."""
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="Springfield",
            state="SP",
            zip_code=12345,
            country_iso_code="USA",
        )

    def test_address_str(self):
        """Test the string representation of the Address model."""
        self.assertEqual(str(self.address), "123 Main St")

    def test_address_fields(self):
        """Test that Address fields are correctly assigned."""
        self.assertEqual(self.address.city, "Springfield")
        self.assertEqual(self.address.state, "SP")
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, "USA")


class LettingModelTest(TestCase):
    """
    Test case for the Letting model.

    Verifies the OneToOne relationship with Address and string representation.
    """

    def setUp(self):
        """Create a sample Letting instance for testing."""
        self.address = Address.objects.create(
            number=456,
            street="Elm St",
            city="Shelbyville",
            state="SH",
            zip_code=54321,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Cozy Apartment", address=self.address
        )

    def test_letting_str(self):
        """Test the string representation of the Letting model."""
        self.assertEqual(str(self.letting), "Cozy Apartment")

    def test_letting_address_relation(self):
        """Test the OneToOne relation between Letting and Address."""
        self.assertEqual(self.letting.address.street, "Elm St")


# =======================
# TESTS DES VUES ET URLS
# =======================
class LettingsViewsTest(TestCase):
    """
    Integration tests for lettings views and URLs.

    Verifies that the index and detail pages render correctly and return the expected status codes.
    """

    def setUp(self):
        """Create a client and sample data for view tests."""
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street="First St",
            city="Metropolis",
            state="MT",
            zip_code=11111,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(title="Luxury Flat", address=self.address)

    def test_lettings_index_view_status_code(self):
        """
        Test the lettings index page returns 200 and uses the correct template.
        Also checks that the created letting appears in the response.
        """
        url = reverse("lettings:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "Luxury Flat")

    def test_letting_detail_view_status_code(self):
        """
        Test the letting detail page returns 200, uses the correct template,
        and displays the correct data for the letting and its address.
        """
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, "Luxury Flat")
        self.assertContains(response, "First St")

    def test_letting_detail_view_not_found(self):
        """
        Test that accessing a non-existing letting returns a 404 status code.
        """
        url = reverse("lettings:letting", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
