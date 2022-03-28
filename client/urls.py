from django.urls import path
from .views import *

urlpatterns = [
    path('index/',NewUserView.as_view(), name='index'),
    path('view/',ListUserView.as_view(),name='user-view'),
    path("update/<int:pk>", UpdateUserView.as_view(), name="user-update"),
    path("detail/<int:pk>", DetailUserView.as_view(), name="user-detail"),
    path("delete/<int:pk>", DeleteUserView.as_view(), name="user-delete")

    # path('about/',about, name='about'),
    # path('blog_grid/',blog_grid, name='blog_grid'),
    # path('blog_sidebar/',blog_sidebar, name = 'blog_sidebar'),
    # path('blog_single/',blog_single, name = 'blog_single'),
    # path('contact/',contact, name = 'contact'),
    # path('pricing/',pricing, name = 'pricing'),
    # path('project/',project, name = 'project'),
    # path('service/',service, name = 'service'),
    # path('feedback/',feedback, name = 'feedback')
]
