from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    
    return HttpResponse('Hello world')


def new(request):
    return HttpResponse('new product')