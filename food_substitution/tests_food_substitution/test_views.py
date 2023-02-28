from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import MyUser
from food_substitution.models import Products, Favorites

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.legal_url = reverse('legal')
        self.user_search_url = reverse('user_search')
        self.fav_page_url = reverse('fav_page')
        self.add_fav_page_url = reverse('add_favorite')
        self.user_search_queries = (
            {'query': 'product_to_db_test'},
            {'query': ''},
            {'query': 'qsdfghjk'},
            {'query': 'boissons'}
            )
        self.user = MyUser.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='12345'
        )
        self.product_to_db_test = Products.objects.create(
            id=1,
            name='product_to_db_test',
            nustriscore='a',
            store='',
            categories='really_good',
            image='beautiful_image.jpg',
            nutritional_guidelines={'salt':'moderate', 'fat':'moderate', 'sugars':'moderate', 'saturated-fat':'moderate'},
            url='https://www.google.com/'
            )

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_substitution/home.html')

    def test_legal_view_page(self):
        response = self.client.get(self.legal_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_substitution/legal_notices.html')

    def test_product_page(self):
        product_page_url = reverse('product_page', kwargs={'num_id':1})
        response = self.client.get(product_page_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_substitution/product.html')

    def test_user_search_page(self):
        for query in self.user_search_queries:
            response = self.client.get(self.user_search_url, query)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'food_substitution/search_aliment.html')
    
    def test_connected_user_add_favourite(self):
        self.client.login(email='test@test.com', password='12345')
        response = self.client.get(self.user_search_url, {'query': 'product_to_db_test'})
        self.assertFalse(Favorites.objects.count())
        self.assertEquals(response.status_code, 200)
        response = self.client.post(self.add_fav_page_url, {'prodId': self.product_to_db_test.id})
        self.assertEquals(response.status_code, 302)
        self.assertTrue(Favorites.objects.count())