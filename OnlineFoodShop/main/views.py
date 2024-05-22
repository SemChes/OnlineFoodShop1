from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
        'content': 'Онлайн продуктовый магазин'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Этот сайт мы скатали из видео курса на рандомном канале'
    }

    return render(request, 'main/about.html', context)
