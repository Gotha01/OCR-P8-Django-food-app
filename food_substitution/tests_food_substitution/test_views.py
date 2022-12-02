from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import MyUser
from food_substitution.models import Products, Favorites

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.user_search_get_url = reverse('user_search')
        self.user_search_post_url = reverse('fav_page')
        self.user_search_queries = (
            {'query': 'nutella'},
            {'query': ''},
            {'query': 'qsdfghjk'}
            )

        self.product_to_db_test = Products.objects.create(
            name='product_to_db_test',
            nustriscore='a',
            store='',
            categories='really_good',
            image='beautiful_image.jpg',
            nutritional_guidelines={'salt':'moderate'},
            url='https://www.google.com/'
            )
        self.get_product = Products.objects.get(name='product_to_db_test')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_substitution/home.html')

    def test_user_search_page_GET(self):
        for query in self.user_search_queries:
            response = self.client.get(self.user_search_get_url, query)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'food_substitution/search_aliment.html')
    
    def test_connected_user_search_POST(self):
        self.user = MyUser.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345'
            )
        self.client.login(email='test@test.com', password='12345')
        response = self.client.post(self.user_search_post_url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'food_substitution/favorite_list.html')