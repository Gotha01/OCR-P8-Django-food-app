from django.shortcuts import render
from PIL import Image
import os

from purbeurre.settings import BASE_DIR

def home(request):
    return render(request, "food_substitution/home.html")

def searching_page(request):
    inPath = BASE_DIR / "assets/img/portfolio/fullsize"
    list_of_images = os.listdir(inPath)
    print(type(list_of_images))
    return render(request, "food_substitution/search_aliment.html", list_of_images)