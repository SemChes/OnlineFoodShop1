from django.shortcuts import render
from catalog.models import Products


def catalog(request, category_slug):
    products = Products.objects.filter(category__slug=category_slug)

    context = {
        'title': 'Главная',
        'content': 'Онлайн продуктовый магазин',
        'catalog': products
    }

    return render(request, 'catalog/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'catalog/product.html', context=context)
