from django.test import TestCase
from django.urls import reverse, resolve
from food_substitution.views import home, user_search_page, add_favorite, favorite_list_page, product_page


class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_user_search_page_url_is_resolved(self):
        url = reverse('user_search')
        self.assertEquals(resolve(url).func, user_search_page)

    def test_product_page_page_url_is_resolved(self):
        url = reverse('product_page', args=[0])
        self.assertEquals(resolve(url).func, product_page)
    
    def test_add_favorite_url_is_resolved(self):
        url = reverse('add_favorite')
        self.assertEquals(resolve(url).func, add_favorite)
    
    def test_favorite_list_page_url_is_resolved(self):
        url = reverse('fav_page')
        self.assertEquals(resolve(url).func, favorite_list_page)