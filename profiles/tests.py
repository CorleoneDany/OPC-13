from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your tests here.


class ProfilesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='Test User',
            password='12345'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Profiles</title>")
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile(self):
        response = self.client.get(reverse('profiles:profile', args={self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Test User</title>")
        self.assertTemplateUsed(response, "profiles/profile.html")
