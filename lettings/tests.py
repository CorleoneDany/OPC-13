from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting

# Create your tests here.


class LettingTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street="Test Street",
            city="Test City",
            state="Test State",
            zip_code=12345,
            country_iso_code="Test Country Code"
        )
        self.letting = Letting.objects.create(
            title="Test Title",
            address=self.address
        )

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Lettings</title>")
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting(self):
        response = self.client.get(reverse('lettings:letting', kwargs={
                                   'letting_id': self.letting.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Test Title</title>")
        self.assertTemplateUsed(response, "lettings/letting.html")
