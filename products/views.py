from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_products(request):
    products = Product.objects.filter(price="10")
    categories = Category.objects.all()
    return render(request, "products.html", {"products": products,
                                             "categories": categories})


def product_home(request):
    products = Product.objects.all().order_by("name")
    categories = Category.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, "product_home.html", {"products": products,
                                                 "categories": categories,
                                                 "items": items,
                                                 "page_range": page_range, })


def products_detail(request, product_slug):
    products = Product.objects.all()
    if product_slug:
        products = get_object_or_404(Product, slug=product_slug)

    return render(request, "products_detail.html", {"products": products})


def all_categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def products_by_category(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.all().order_by("name")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, "product_home.html", {"products": products,
                                                 "categories": categories,
                                                 "items": items,
                                                 "page_range": page_range, })