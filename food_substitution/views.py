from django.shortcuts import render
from django.db.models import Q

from food_substitution.models import Products

def replace_artefacts(list_to_correct):
    cleaned_list = []
    for element in list_to_correct:
        cleaned_element = element.replace("'","").replace(" ","").replace("[","").replace("]","")
        cleaned_list.append(cleaned_element)
    return cleaned_list
    
def home(request):
    return render(request, "food_substitution/home.html")
    
def user_search_page(request):
    products = Products.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query is not None:
            products = Products.objects.filter(
                Q(name__icontains=query)|Q(categories__icontains=query))
            lenproducts = str(len(products))
    context = {"products": products,
               "lenproducts": lenproducts}

    return render(request,
                "food_substitution/search_aliment.html",
                context)
        

def product_page(request, num_id):
    product = Products.objects.get(id=num_id)
    guidelines = product.nutritional_guidelines
    guidelines_fr = {
        'graisses':guidelines['fat'],
        'sel':guidelines['salt'],
        'sucres':guidelines['sugars'],
        'graisses_saturees':guidelines['saturated-fat']
    }
    en_v = ['low','moderate','high']
    fr_v = ['peu',' modéré','beaucoup']
    for k,v in guidelines_fr.items():
        if v in en_v :
            guidelines_fr[k]=fr_v[en_v.index(v)]
    return render(request, 
                "food_substitution/product.html",
                {"product": product,
                "guidelines": guidelines_fr})

