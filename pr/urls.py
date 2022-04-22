from django.urls import path
from pr.views import *

urlpatterns=[
    path('canada_pr_form/', NewCanada_prView.as_view(),name="canada_pr_form"),
    path('view/', ListCanada_prView.as_view(), name='canada_pr-view'),
    path("update/<int:pk>", UpdateCanada_prView.as_view(), name="canada_pr-update"),
    path("delete/<int:pk>", DeleteCanada_prView.as_view(), name="canada_pr-delete"),
    path("detail/<int:pk>", DetailCanada_prView.as_view(), name="canada_pr-detail")

]
