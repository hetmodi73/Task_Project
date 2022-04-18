from django.urls import path
from .views import *

urlpatterns = [
    path("signup/",NewSignupView.as_view(), name="signup"),

    path('index/',NewUserView.as_view(), name='index'),
    path('view/',ListUserView.as_view(),name='user-view'),
    path("update/<int:pk>", UpdateUserView.as_view(), name="user-update"),
    path("detail/<int:pk>", DetailUserView.as_view(), name="user-detail"),
    path("delete/<int:pk>", DeleteUserView.as_view(), name="user-delete")
]
