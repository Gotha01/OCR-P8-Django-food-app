from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_page_view = reverse('login')
        self.change_profile = reverse('change_profile')
        self.change_password = reverse('change_password')
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com',
            username='testuser',
            password='testpass'
        )
        self.data = {
            'old_password': 'testpass',
            'new_password1': 'newtestpass',
            'new_password2': 'newtestpass'
        }

    def test_user_connection_get(self):
        response = self.client.get(self.login_page_view)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        
    def test_user_change_authenticated(self):
        self.client.login(email='testuser@test.com', password='testpass')
        response = self.client.get(self.change_profile)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/modify_user.html')
        data = {'username': 'new_username', 'email': 'new_email@example.com'}
        response = self.client.post(self.change_profile, data=data)
        self.assertRedirects(response, reverse('profile_page'))
        self.user.refresh_from_db()
        self.assertEquals(self.user.username, 'new_username')
        self.assertEquals(self.user.email, 'new_email@example.com')

    def test_user_change_password(self):
        self.client.login(email='testuser@test.com', password='testpass')
        response = self.client.post(self.change_password, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newtestpass'))