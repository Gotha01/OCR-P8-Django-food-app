from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_page_view = reverse('login')

    def test_user_connection_get(self):
        response = self.client.get(self.login_page_view)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')