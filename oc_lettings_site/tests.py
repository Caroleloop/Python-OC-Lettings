from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from . import views


# =======================
# TESTS DES VUES
# =======================
class OCLettingsSiteViewsTest(TestCase):
    """
    Unit and integration tests for the views of 'oc_lettings_site'.
    """

    def setUp(self):
        """
        Initialize a test client for sending HTTP requests to views.
        """
        self.client = Client()

    def test_index_view_status_code_and_template(self):
        """
        Verify that the index view returns HTTP 200 and uses 'index.html'.
        """
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_custom_404_view_status_code_and_template(self):
        """
        Verify that the custom 404 view returns HTTP 404 and the 404 template.
        """
        request = HttpRequest()
        response = views.custom_404(request, Exception("Not found"))
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"404", response.content or b"")

    def test_custom_500_view_status_code_and_template(self):
        """
        Verify that the custom 500 view returns HTTP 500 and the 500 template.
        """
        request = HttpRequest()
        response = views.custom_500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"500", response.content or b"")


# =======================
# TESTS DES URLS
# =======================
class OCLettingsSiteURLsTest(TestCase):
    """
    Tests for verifying that the main URLs of the application work correctly.
    """

    def test_root_url_resolves_to_index(self):
        """
        The root URL ('/') should resolve to the index view.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_admin_url(self):
        """
        The '/admin/' URL should respond with status 200 (if admin accessible)
        or 302 redirect to login page if no superuser exists.
        """
        response = self.client.get("/admin/")
        self.assertIn(response.status_code, [200, 302])
