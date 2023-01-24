# -*- coding: utf-8 -*-
import requests
import logging
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from food_substitution.models import Products, Favorites

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Incrementing the PurBeurre application database"

    def add_arguments(self, parser):
        parser.add_argument(
            'category', 
            type=str,
            help='Name of the category name to be added to the database. (min. 3 caracters).'
            )
        parser.add_argument(
            '--nbr_datas', 
            type=int, 
            default=100, 
            help="Number of product per category (min. 50 products)."
            )
        parser.add_argument(
            '--upgrade',
            default=None,
            help="Overwrite old data if not in a user favorite products list"
        )
        
    def handle(self, *args, **options):
        """From argument, increment the app's database using category names

        Raises:
            CommandError: 'Category element' must be longer than 3 caracters
            CommandError: --nbr_datas must be greater than 50
        """
        
        class Etl():
            def __init__(self, categories_list, number_of_products):
                self.categories_list = categories_list
                self.value_features = [
                    'product_name_fr',
                    'nutrition_grades',
                    'stores',
                    'categories_hierarchy',
                    'image_front_url',
                    'nutrient_levels',
                    'url']
                self.nbr_datas = str(number_of_products)
                self.querycat = self.extract_from_catname()
                self.count = self.transform_and_load()
                logger.error(f"{self.count} products have been added to the database.")
                
            def extract_from_catname(self):
                """Function to get json file with all products from OpenFoodFacts."""
                prod_caracteristics = []
                for element in self.categories_list:
                    get_1 = "https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0='"
                    get_2 = "'&tagtype_1=languages&tag_contains_1=contains&tag_1=fr&page_size="
                    get_3 = "&search_simple=1&action=process&json=1"
                    categreq = requests.get(get_1 + element + get_2 + self.nbr_datas + get_3).json()
                    prodrec = (categreq['products'])
                    for product in prodrec:
                        find_product = {}
                        caracs = product.keys()
                        if "France" in product['countries']:
                            for feature in self.value_features:
                                for carac in caracs:
                                    if carac == feature:
                                        find_product[carac] = product[carac]
                            prod_caracteristics.append(find_product)
                return prod_caracteristics

            def transform_and_load(self):
                """Function to transform the data and prepare it before loading it into the database """
                iteration_count = 0
                for element in self.querycat:
                    if len(element)==len(self.value_features):
                        dropper = ['en:', 'fr:']
                        elecat = element['categories_hierarchy']
                        for category in elecat:
                            catindex = elecat.index(category)
                            if (category[0:3] in dropper):
                                elecat[catindex] = category[3:-1]
                        if element['nutrition_grades'] in ['a','b','c','d','e'] and\
                            element['product_name_fr'] != '' and\
                            '\n' not in element['product_name_fr']:
                            try:
                                _ = Products.objects.get(name=element['product_name_fr'])
                            except ObjectDoesNotExist:
                                p = Products(
                                    name=element['product_name_fr'],
                                    nustriscore=element['nutrition_grades'],
                                    store=element['stores'],
                                    categories=element['categories_hierarchy'],
                                    image=element['image_front_url'],
                                    nutritional_guidelines=element['nutrient_levels'],
                                    url=element['url'])
                                p.save()
                                iteration_count += 1
                return iteration_count

        class Del_data():
            def __init__(self):
                self.favorite_id_list = []
                self.all_products = Products.objects.all()
                self.all_favorites = Favorites.objects.all()
                self.search_for_non_favorite_products()
                logger.error("All unregistered data have been deleted", extra={'number of data':len(Products.objects.all())})

            def search_for_non_favorite_products(self):
                for favorite in self.all_favorites:
                    self.favorite_id_list.append(favorite.products.id)
                for product in self.all_products:
                    if product.id not in self.favorite_id_list:
                        target_product = Products.objects.get(id=product.id)
                        target_product.delete()

        len_ok = False
        categories = options['category'].split(',')
        nbr_datas = options['nbr_datas']
        upgrade = options['upgrade']
        if upgrade == 'True':
            Del_data()
        if nbr_datas > 2:
            for element in categories:
                if len(element) >= 3:
                    len_ok = True
                else:
                    raise CommandError("'Category element' must be longer than 3 caracters")
            if len_ok:  
                Etl(categories, nbr_datas)
        else:
            raise CommandError("--nbr_datas must be greater than 3")