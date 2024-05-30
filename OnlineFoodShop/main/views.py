from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Главная',
        'content': 'Онлайн продуктовый магазин',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Этот сайт мы скатали из видео курса на рандомном канале'
    }

    return render(request, 'main/about.html', context)
