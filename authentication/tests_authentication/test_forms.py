from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from authentication.forms import LoginForm, SignupForm


class TestForms(SimpleTestCase):
    
    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username' : 'tester',
            'password' : 'tester_password_1234'
        })
        self.assertTrue(form.is_valid())

class SignupFormTest(TestCase):

    def test_signup_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form_data = {
            'email': '',
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())