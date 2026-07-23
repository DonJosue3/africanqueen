from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('home/',views.home,name="home"),
    path("services/", views.services, name="services"),
    path("menu/", views.menu, name="menu"),
    path("shop/", views.shop, name="shop")
]