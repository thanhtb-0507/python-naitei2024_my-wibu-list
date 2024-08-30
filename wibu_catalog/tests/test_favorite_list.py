from django.urls import reverse
from django.test import TestCase, Client
from django.utils import timezone
from wibu_catalog.models import Users, Content, FavoriteList
from django.contrib.auth.models import AnonymousUser

class FavoriteListViewTest(TestCase):
    def setUp(self):
        # Create user
        self.user = Users.objects.create(
            uid=1,
            username='test_user',
            email='test@example.com',
            password='password123',
            registrationDate=timezone.now(),
        )

        # Create content
        self.content1 = Content.objects.create(
            cid=1,
            name='Favorite Anime 1',
            category='anime',
            scoreAvg=8.0
        )
        self.content2 = Content.objects.create(
            cid=2,
            name='Favorite Anime 2',
            category='anime',
            scoreAvg=9.0
        )

        # Create favorite list
        FavoriteList.objects.create(
            uid=self.user,
            cid=self.content1,
            status='1',
            progress=5
        )
        FavoriteList.objects.create(
            uid=self.user,
            cid=self.content2,
            status='2',
            progress=10
        )

        self.client = Client()
        self.client.force_login(self.user)

    def test_favorite_list_view_with_favorites(self):
        response = self.client.get(reverse('favorites_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/favorites_list.html')
        self.assertIn('favorites_list', response.context)
        self.assertIn('userr', response.context)
        self.assertEqual(len(response.context['favorites_list']), 2)

    def test_favorite_list_view_without_favorites(self):
        # Remove favorites
        FavoriteList.objects.all().delete()
        response = self.client.get(reverse('favorites_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/favorites_list.html')
        self.assertIn('favorites_list', response.context)
        self.assertIn('userr', response.context)
        self.assertEqual(len(response.context['favorites_list']), 0)
