from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search.html", {"products": products})