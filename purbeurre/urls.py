from django.contrib import admin
from django.urls import path

from authentication import views as authv
from food_substitution import views as fsv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fsv.home, name='home'),
    path('login/', authv.LoginPageView.as_view(), name="login"),
    path('logout/', authv.logout_user, name='logout'),
    path('signup/', authv.signup_page, name='signup'),
    path('search/', fsv.user_search_page, name="user_search"),
    path('search/<int:num_id>/', fsv.product_page, name="product_page"),
    path('profile/', authv.profile_page, name="profile_page"),
    path('addfavorite/', fsv.add_favorite, name='add_favorite'),
    path('favorite/', fsv.favorite_list_page, name="fav_page"),
    path('legal/', fsv.legal_view, name='legal')
]