from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product.title)
    # query_set = Product.objects.filter(price__range=(20,30))
    # query_set = Product.objects.filter(title__icontains='coffee')
    # Q OBJECT EXAMPLE
    query_set = Product.objects.filter(Q(inventory__lt=10) |Q(price__lt=20))
    # ~Q is like not Q


    # print(query_set[0:5]) show first 5 rows
  
    # list(query_set.values()) show them on the list
    return render(request, 'hello.html', {'name': 'Dren', 'products': list(query_set)})