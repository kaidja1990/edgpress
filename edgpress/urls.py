from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('index.html', index, name='index'),
    path('basic-grid.html/', basic_grid, name='basic-grid'),
    path('full-width.html', full_width, name='full-width'),
    path('gallery.html', gallery, name='gallery'),
    path('sidebar-right.html', sidebar_right, name='sidebar-right'),
    path('sidebar-left.html', sidebar_left, name='sidebar-left')
]

