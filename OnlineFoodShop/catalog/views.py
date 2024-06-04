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


def product(request):
    return render(request, 'catalog/product.html')
