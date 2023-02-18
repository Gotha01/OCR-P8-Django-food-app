from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import MyUser

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.signup_url = reverse('signup')
        self.profile_url = reverse('profile_page')
        self.user = MyUser.objects.create_user(email='test@test.test',username='testuser', password='testpass')
    
    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
    
    def test_login_view_POST_valid_credentials(self):
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
    
    def test_login_view_POST_invalid_credentials(self):
        data = {'username': 'invalid', 'password': 'invalid'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    
    def test_logout_view(self):
        self.client.login(email='test@test.test',username='testuser', password='testpass')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, reverse('home'), status_code=302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    
    def test_signup_view_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')
    
    def test_signup_view_POST_invalid_credentials(self):
        data = {'username': 'newuser', 'password1': 'testpass', 'password2': 'invalid'}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    
    def test_profile_view_authenticated_user(self):
        self.client.login(email='test@test.test',username='testuser', password='testpass')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)