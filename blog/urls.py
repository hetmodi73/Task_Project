from django.urls import path
from .views import *

urlpatterns = [
    path('blog_grid/',blog_grid, name='blog_grid'),
    path('blog_sidebar/',blog_sidebar, name = 'blog_sidebar'),
    path('blog_single/',blog_single, name = 'blog_single')
]
