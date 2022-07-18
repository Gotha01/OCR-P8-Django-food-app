from django.db import models

class Products(models.Model):

    nustriscore_choices = [
        ("a","A"),
        ("b","B"),
        ("c","C"),
        ("d","D"),
        ("e","E")
    ]

    name = models.CharField(max_length=120, unique=True)
    nustriscore = models.CharField(choices=nustriscore_choices, max_length=1)
    store = models.CharField(max_length=50, null=True)
    categories = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products")
    nutritional_guidelines = models.JSONField()
    url = models.URLField(max_length=200)