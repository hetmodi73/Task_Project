from django.urls import path
from .views import *

urlpatterns=[
    path('service/', service, name='service')

]