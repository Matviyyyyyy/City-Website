from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class AdvertListTest(TestCase):
    def test_ping(self):
        url = reverse('adverts:advert-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)