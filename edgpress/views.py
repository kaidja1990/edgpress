from django.shortcuts import render
from .models import *


def index(request):
    all_articles = Article.objects.all()
    context = {
        "article": all_articles
    }
    return render(request, 'edgpress/index.html', context)


def basic_grid(request):
    return render(request, 'edgpress/basic-grid.html')


def gallery(request):
    return render(request, 'edgpress/gallery.html')


def full_width(request):
    return render(request, 'edgpress/full-width.html')


def sidebar_left(request):
    return render(request, 'edgpress/sidebar-left.html')


def sidebar_right(request):
    return render(request, 'edgpress/sidebar-right.html')

