from django.urls import reverse
from django.test import TestCase, Client
from django.utils.decorators import decorator_from_middleware
from django.http import HttpResponse
from django.shortcuts import redirect
from wibu_catalog.views import require_login
from wibu_catalog.models import Users

class RequireLoginDecoratorTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Users.objects.create(
            uid=1,
            username='test_user',
            email='test@example.com',
            password='password123',
            registrationDate=timezone.now(),
        )
        self.login_url = reverse('login')  # Replace with your actual login URL

    def test_require_login_decorator_logged_in(self):
        @require_login
        def view_func(request):
            return HttpResponse('You are logged in.')

        self.client.force_login(self.user)
        response = self.client.get(reverse('some_protected_view'))  # Replace with your actual view URL
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'You are logged in.')

    def test_require_login_decorator_not_logged_in(self):
        @require_login
        def view_func(request):
            return HttpResponse('You are logged in.')

        response = self.client.get(reverse('some_protected_view'))  # Replace with your actual view URL
        self.assertRedirects(response, self.login_url)
