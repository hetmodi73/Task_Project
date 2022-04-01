from django.db import models
from django.urls import reverse
from client .models import user
from services .models import service, service_details
# Create your models here.

class document(models.Model):
    # DOCUMENT_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='document')
    DOCUMENT_NAME=models.CharField(max_length=20)
    DOCUMENT_FILE=models.FileField(default="",upload_to="profile", blank=True,null=True)
    services=models.ForeignKey(service,on_delete=models.CASCADE, related_name='document', blank=True,null=True)

    def __str__(self):
        return f"{self.client}-{self.services}"

    def get_absolute_url(self):
        return reverse('document-view')

class master_question(models.Model):
    # QUESTION_ID=models.IntegerField(null=True)
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    services=models.ForeignKey(service_details,on_delete=models.CASCADE, related_name='master_question', blank=True,null=True)

    def __str__(self):
        return f"{self.services}"

    def get_absolute_url(self):
        return reverse('master_question-view')

class sub_question(models.Model):
    # SUB_QUESTION_ID=models.IntegerField(null=True)
    QUESTION_ID=models.ForeignKey(master_question,on_delete=models.CASCADE, related_name='sub_question', blank=True,null=True)
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    services=models.ForeignKey(service_details,on_delete=models.CASCADE, related_name='sub_question', blank=True,null=True)

    def __str__(self):
        return f"{self.QUESTION_ID}-{self.services}"

    def get_absolute_url(self):
        return reverse('sub_question-view')
