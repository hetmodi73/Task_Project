from django.urls import path
from .views import *

urlpatterns=[
    path('service/', NewServiceView.as_view(), name='service'),
    path('view/', ListServiceView.as_view(), name='service-view'),
    path("update/<int:pk>", UpdateServiceView.as_view(), name="service-update"),
    path("detail/<int:pk>", DetailServiceView.as_view(), name="service-detail"),
    path("delete/<int:pk>", DeleteServiceView.as_view(), name="service-delete"),

    path('service/', NewService_detailsView.as_view(), name='service'),
    path('view/', ListService_detailsView.as_view(), name='service_details-view'),
    path("update/<int:pk>", UpdateService_detailsView.as_view(), name="service_details-update"),
    path("detail/<int:pk>", DetailService_detailsView.as_view(), name="service_details-detail"),
    path("delete/<int:pk>", DeleteService_detailsView.as_view(), name="service_details-delete")
]
