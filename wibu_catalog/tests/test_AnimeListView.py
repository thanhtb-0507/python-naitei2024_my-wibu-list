from django.test import TestCase, RequestFactory
from django.urls import reverse
from wibu_catalog.models import Users, Content
from wibu_catalog.views import AnimeListView, _get_user_from_session
from unittest.mock import patch

class AnimeListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = Users.objects.create(uid=1, username='test_user')
        self.content1 = Content.objects.create(cid=1, name='Anime 1', category='anime')
        self.content2 = Content.objects.create(cid=2, name='Anime 2', category='anime')
        self.content3 = Content.objects.create(cid=3, name='Manga 1', category='manga')

    @patch('wibu_catalog.views._get_user_from_session')
    def test_anime_list_view(self, mock_get_user):
        mock_get_user.return_value = self.user
        request = self.factory.get(reverse('anime_list'))
        request.session = {'user_id': self.user.uid}

        response = AnimeListView.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Anime 1')
        self.assertContains(response, 'Anime 2')
        self.assertNotContains(response, 'Manga 1')
        self.assertEqual(response.context_data['userr'], self.user)
