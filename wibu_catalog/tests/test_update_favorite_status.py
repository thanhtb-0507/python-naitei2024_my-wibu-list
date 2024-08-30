from django.test import TestCase, Client
from django.urls import reverse
from wibu_catalog.models import Users, Content, FavoriteList

class UpdateFavoriteStatusViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        # Create a user with a password
        self.user = Users.objects.create(
            uid=1,
            username='test_user',
            email='test_user@example.com',
            password='test_password'  # Ensure password is set correctly
        )

        # Set password for the user to match the login credentials
        self.user.set_password('test_password')
        self.user.save()

        # Create content
        self.content = Content.objects.create(
            cid=1,
            name='Test Anime',
            category='anime',
            scoreAvg=8.5
        )

    def test_update_favorite_status_valid(self):
        # Log in the user
        self.client.login(username='test_user', password='test_password')

        # Post request to update favorite status
        response = self.client.post(reverse('update_favorite_status', args=[self.content.cid]), {'status': '1'})

        # Check if the redirect status code is 302
        self.assertEqual(response.status_code, 302)

        # Verify that the favorite list entry has been created or updated
        favorite = FavoriteList.objects.get(uid=self.user, cid=self.content)
        self.assertEqual(favorite.status, '1')

    def test_update_favorite_status_not_logged_in(self):
        # Post request without logging in
        response = self.client.post(reverse('update_favorite_status', args=[self.content.cid]), {'status': '1'})

        # Check if the redirect status code is 302, indicating redirection to login
        self.assertEqual(response.status_code, 302)

    def test_update_favorite_status_invalid_status(self):
        # Log in the user
        self.client.login(username='test_user', password='test_password')

        # Post request with an invalid status
        response = self.client.post(reverse('update_favorite_status', args=[self.content.cid]), {'status': '4'})

        # Check if the redirect status code is 302
        self.assertEqual(response.status_code, 302)

        # Verify that no favorite list entry was created or updated
        favorite_exists = FavoriteList.objects.filter(uid=self.user, cid=self.content).exists()
        self.assertFalse(favorite_exists)
