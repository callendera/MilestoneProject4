from django.shortcuts import render
from products.models import Product


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products, "scroll_to_search_results": True})