from purbeurre.settings import AUTH_USER_MODEL
from django.db import models

class Products(models.Model):
    """Product model."""

    nustriscore_choices = [
        ("a","A"),
        ("b","B"),
        ("c","C"),
        ("d","D"),
        ("e","E")
    ]

    name = models.CharField(max_length=120, unique=True)
    nustriscore = models.CharField(choices=nustriscore_choices, max_length=3)
    store = models.CharField(max_length=200, null=True)
    categories = models.CharField(max_length=1500)
    image = models.ImageField(upload_to="products")
    nutritional_guidelines = models.JSONField()
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name[:50]

class Favorites(models.Model):
    """Favorites model."""

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)