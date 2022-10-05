from django.contrib import admin
from food_substitution.models import Products, Favorites

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Favorites)
