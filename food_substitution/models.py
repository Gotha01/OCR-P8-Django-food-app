from django.db import models


class Categories(models.Model):
    Category_name = models.CharField(unique=True)

    def __str__(self):
        return self.Category_name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Categories)