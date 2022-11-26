from django.test import TestCase, Client
from django.urls import reverse
from food_substitution.models import Products, Favorites
import json

"""class TestViews(TestCase):

    def test_user_search_page_GET(self):
        client = Client()
        response = client.get(reverse('user_search'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_substitution/search_aliment.html')"""