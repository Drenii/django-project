from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Max, Min, Count, Avg, Sum

def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product.title)
    # query_set = Product.objects.filter(price__range=(20,30))
    # query_set = Product.objects.filter(title__icontains='coffee')
    # Q OBJECT EXAMPLE
    # query_set = Product.objects.filter(Q(inventory__lt=10) |Q(price__lt=20))
    # ~Q is like not Q
    # F referencing fields, example find all data from db where inventory is equat to price
    # query_set = Product.objects.filter(inventory=F('price'))
    #filter by order
    # query_set = Product.objects.order_by('price', '-title').reverse()
    #Limiting results
    # query_set = Product.objects.all()[:5]
    # SELECTING FIELDS TO QUERY
    # query_set=Product.objects.values_list('id', 'title', 'collection__title')
    # JOIN TWO TABLES
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    result= Product.objects.aggregate(count=Count('id', min_price=Min('price')))
    # print(query_set[0:5]) show first 5 rows
  
    # list(query_set.values()) show them on the list
    # return render(request, 'hello.html', {'name': 'Dren', 'products': list(query_set)})
    return render(request, 'hello.html', {'name': 'Dren', 'results': result}) #this one is useed for aggregation purposes