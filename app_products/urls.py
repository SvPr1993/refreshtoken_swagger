from django.urls import path
from app_products.views import Products, Home


urlpatterns = [
    path('all/', Products.as_view(), name='products'),
    path('home/', Home.as_view(), name='products'),
]