from django.urls import path
from visa.views import *

urlpatterns=[
    path('canada_form/', NewCanadaView.as_view(),name="canada_form"),
    path('view/', ListCanadaView.as_view(), name='canada-view'),
    path("update/<int:pk>", UpdateCanadaView.as_view(), name="canada-update"),
    path("delete/<int:pk>", DeleteCanadaView.as_view(), name="canada-delete"),
    path("detail/<int:pk>", DetailCanadaView.as_view(), name="canada-detail")

]
