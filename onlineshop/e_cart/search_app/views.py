from django.shortcuts import render
from shop.models import Product


def searchResult(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        product = Product.objects.all().filter(name__contains=query)
    return render(request, 'search.html',{'product':product, 'query':query})