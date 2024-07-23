from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.template.loader import get_template
from .models import Products, Catogoery, Reviews

from django.template import loader

# Create your views here.

def products_list(request):
    myproductlist=Products.objects.all().values() # to retrieve all the values
    template=loader.get_template("products.html")
    context={
        "myproductlist":myproductlist,
    }
    return HttpResponse(template.render(context,request))

def catogery_list(request):
    mycatogerylist=Catogoery.objects.all().values() # to retrieve all the values
    template=loader.get_template("catogery.html")
    context={
        "mycatogerylist":mycatogerylist,
    }
    return HttpResponse(template.render(context,request))


def reviews_list(request):
    myreviewlist=Catogoery.objects.all().values() # to retrieve all the values
    template=loader.get_template("reviews.html")
    context={
        "myreviewlist":myreviewlist,
    }
    return HttpResponse(template.render(context,request))

