from django.test import TestCase
from django.urls import reverse, resolve
from authentication.views import logout_user , signup_page, profile_page, change_profile


class TestUrls(TestCase):

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup_page)

    def test_profile_page_url_is_resolved(self):
        url = reverse('profile_page')
        self.assertEquals(resolve(url).func, profile_page)

    def test_favorite_change_profile_url_is_resolved(self):
        url = reverse('change_profile')
        self.assertEquals(resolve(url).func, change_profile)