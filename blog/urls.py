from django.urls import path
from .views import *

urlpatterns = [
    path('blog_grid/', NewDocumentView.as_view(), name='blog_grid'),
    path('view/', ListDocumentView.as_view(), name='document-view'),
    path("update/<int:pk>", UpdateDocumentView.as_view(), name="document-update"),
    path("detail/<int:pk>", DetailDocumentView.as_view(), name="document-detail"),
    path("delete/<int:pk>", DeleteDocumentView.as_view(), name="document-delete"),

    path('blog_sidebar/', NewMaster_questionView.as_view(), name='blog_sidebar'),
    path('view/', ListMaster_questionView.as_view(), name='master_question-view'),
    path("update/<int:pk>", UpdateMaster_questionView.as_view(), name="master_question-update"),
    path("detail/<int:pk>", DetailMaster_questionView.as_view(), name="master_question-detail"),
    path("delete/<int:pk>", DeleteMaster_questionView.as_view(), name="master_question-delete"),

    path('blog_single/', NewSub_questionView.as_view(), name = 'blog_single'),
    path('view/', ListSub_questionView.as_view(), name='sub_question-view'),
    path("update/<int:pk>", UpdateSub_questionView.as_view(), name="sub_question-update"),
    path("detail/<int:pk>", DetailSub_questionView.as_view(), name="sub_question-detail"),
    path("delete/<int:pk>", DeleteSub_questionView.as_view(), name="sub_question-delete")

]
