from django.test import SimpleTestCase
from authentication.forms import LoginForm, SignupForm


class TestForms(SimpleTestCase):

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username' : 'tester',
            'password' : 'tester_password_1234'
        })
        self.assertTrue(form.is_valid())
