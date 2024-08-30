from django.test import TestCase
from django.urls import reverse
from wibu_catalog.models import Content, Users
from unittest.mock import patch
from django.utils import timezone

class HomepageViewTest(TestCase):
    def setUp(self):
        self.user1 = Users.objects.create(
            uid=1,
            username="UserOne",
            email="userone@example.com",
            password="password123",
            registrationDate=timezone.now(),
        )

        # Create some Content objects
        self.content1 = Content.objects.create(
            cid=1,
            name='Test Anime 1',
            watching=100,
            lastUpdate="2024-08-28",
            ranked=1,
            category='anime'
        )
        self.content2 = Content.objects.create(
            cid=2,
            name='Test Anime 2',
            watching=200,
            lastUpdate="2024-08-29",
            ranked=2,
            category='anime'
        )
        self.content3 = Content.objects.create(
            cid=3,
            name='Test Anime 3',
            watching=300,
            lastUpdate="2024-08-30",
            ranked=3,
            category='anime'
        )

    @patch('wibu_catalog.views.random_button')
    def test_homepage_view(self, mock_random_button):
        # Mock the random_button to return content1
        mock_random_button.return_value = self.content1

        # Use the Django test client to make a request
        session = self.client.session
        session['user_id'] = self.user1.uid
        session.save()  # Don't forget to save the session!

        response = self.client.get(reverse('homepage'))

        # Check the response status
        self.assertEqual(response.status_code, 200)

        # Check if the correct template was used
        self.assertTemplateUsed(response, 'html/homepage.html')

        # Check if the context data is correct
        self.assertIn('top_watching_content', response.context)
        self.assertIn('latest_content', response.context)
        self.assertIn('top_ranked_content', response.context)
        self.assertIn('userr', response.context)
        self.assertIn('what_to_watch', response.context)

        # Verify the contents of the context data
        self.assertListEqual(
            list(response.context['top_watching_content']),
            list(Content.objects.order_by('-watching')[:3])
        )
        self.assertListEqual(
            list(response.context['latest_content']),
            list(Content.objects.order_by('-lastUpdate')[:3])
        )
        self.assertListEqual(
            list(response.context['top_ranked_content']),
            list(Content.objects.order_by('ranked')[:3])
        )
        self.assertEqual(response.context['userr'], self.user1)
        self.assertEqual(response.context['what_to_watch'], self.content1)
