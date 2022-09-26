from django.test import TestCase
from django.urls import reverse

class TestFetchView(TestCase):

    def test_fetch_view_response(self):

        response = self.client.get(reverse("fetch"))
        self.assertEqual(response.status_code, 200)
