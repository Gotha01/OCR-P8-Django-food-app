from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from food_substitution.models import Products
from food_substitution.models import Favorites

def replace_artefacts(list_to_correct):
    cleaned_list = []
    for element in list_to_correct:
        cleaned_element = element.replace("'","").replace(" ","").replace("[","").replace("]","")
        cleaned_list.append(cleaned_element)
    return cleaned_list
    
def home(request):
    return render(request, "food_substitution/home.html")
    
def user_search_page(request):
    cat_dict, favorites_id_list, filters_c = {}, [], [" '","'"]
    final_category_list = []
    if request.method == "GET":
        query = request.GET.get('query')
        prodId = request.GET.get('prodId')
        if query is not None:
            if prodId is not None:
                current_user = request.user
                product = Products.objects.get(id=prodId)
                new_favorite, _ = Favorites.objects.get_or_create(
                user_id=current_user.id,
                products=product
                )
            dir_products = Products.objects.filter(
                Q(name__icontains=query)|
                Q(categories__icontains=query))
            for element in dir_products.values():
                bad_cat_str_list = element['categories']
                for c in filters_c:
                    cat_str_list = bad_cat_str_list.replace(c,"")
                cat_list = cat_str_list[1:-1].split(', ')
                for categorie in cat_list:
                    if categorie in cat_dict.keys():
                        cat_dict[categorie]+=1
                    else:
                        cat_dict[categorie]=1
            list_val = list(cat_dict.values())
            list_val.sort()
            max_cat_index = (list_val[-1],list_val[-2])
            for k,v in cat_dict.items():
                if v in max_cat_index:
                    final_category_list.append(k)
            filter_products = Products.objects.filter(
                Q(name__icontains=query)
                )
            for element in final_category_list:
                dab = Products.objects.filter(Q(categories__icontains=element))
                final_products = filter_products.union(dab).order_by('nustriscore')
            lenproducts = str(len(final_products))
        favorites = Favorites.objects.filter(user_id__exact=request.user.id)
        if len(favorites) != 0:
            for element in favorites.values():
                favorites_id_list.append(element['products_id'])
        context = {
            'query': query,
            'products': final_products,
            'lenproducts': lenproducts,
            'favorites_id_list': favorites_id_list
                }
        return render(
            request,
            "food_substitution/search_aliment.html",
            context
            )

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
    fr_v = ['peu','modérée','beaucoup']
    for k,v in guidelines_fr.items():
        if v in en_v :
            guidelines_fr[k]=fr_v[en_v.index(v)]
    return render(request, 
                'food_substitution/product.html',
                {'product': product,
                'guidelines': guidelines_fr})

@login_required
def favorite_list_page(request):
    fav_id_list = []
    current_user = request.user
    user_fav = Favorites.objects.filter(user=current_user)
    for fav in user_fav.values():
        fav_id_list.append(fav['products_id'])
    user_fav_prod = Products.objects.filter(id__in=fav_id_list)
    print(user_fav_prod)
    context={
        "user": current_user,
        "user_fav_prod": user_fav_prod,
        }
    return render(
        request,
        'food_substitution/favorite_list.html',
        context
        )