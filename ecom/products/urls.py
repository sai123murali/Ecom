
from .models import Products,Catogoery,Reviews
from . import views
from django.contrib.auth.urls import urlpatterns

from django.urls import path

urlpatterns=[
    path('products/',views.products_list,name="Products"),
    path('catogery/',views.catogery_list,name="Catogoery"),
    path('reviews/',views.reviews_list,name="Reviews"),
]