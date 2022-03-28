from django.urls import path
from .views import *

urlpatterns = [
    path('feedback/',NewFeedbackView.as_view(), name = 'feedback'),
    path('view/', ListFeedbackView.as_view(), name='feedback-view'),
    path("update/<int:pk>", UpdateFeedbackView.as_view(), name="feedback-update"),
    path("delete/<int:pk>", DeleteFeedbackView.as_view(), name="feedback-delete"),
    path("detail/<int:pk>", DetailFeedbackView.as_view(), name="feedback-detail")
]
