from django.urls import path
from app_products.views import Products


urlpatterns = [
    path('all/', Products.as_view(), name='products'),
]