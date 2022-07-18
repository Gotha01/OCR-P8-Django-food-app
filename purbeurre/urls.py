"""purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication import views as authv
from food_substitution import views as fsv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fsv.home, name='home'),
    path('login/',authv.login_page, name="login"),
    path('logout/', authv.logout_user, name="logout"),
    path('search/', fsv.searching_page, name="search"),
    path('profile/', authv.profile_page, name="profile_page"),
]