from django.shortcuts import render
from catalog.models import Products


def catalog(request):
    products = Products.objects.all()

    context = {
        'title': 'Главная',
        'content': 'Онлайн продуктовый магазин',
        'catalog': products
    }

    return render(request, 'catalog/catalog.html', context)


def product(request, product_id):

    product = Products.objects.get(id=product_id)

    context = {
        'product': product
    }

    return render(request, 'catalog/product.html', context=context)
