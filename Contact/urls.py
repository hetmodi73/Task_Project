from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', NewContactView.as_view(), name = 'contact'),
    path('view/', ListContactView.as_view(), name= 'contact-view'),
    path("update/<int:pk>", UpdateContactView.as_view(), name="contact-update"),
    path("delete/<int:pk>", DeleteContactView.as_view(), name="contact-delete"),
    path("detail/<int:pk>", DetailContactView.as_view(), name="contact-detail")
]
