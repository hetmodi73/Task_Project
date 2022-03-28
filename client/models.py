from django.db import models
from django.urls import reverse

# Create your models here.

class user(models.Model):
    # L_ID=models.IntegerField(null=True)
    EMAIL_ID=models.CharField(max_length=25)
    PHONE_NO=models.IntegerField()
    PASSWORD=models.CharField(max_length=25)
    NAME=models.CharField(max_length=25)
    choice1=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    GENDER=models.CharField(max_length=25,choices=choice1)
    ADDRESS=models.TextField(max_length=25)
    ROLE=models.IntegerField()
    choice2=(
        ('ACTIVE','ACTIVE'),
        ('INACTIVE','INACTIVE')
    )
    STATUS=models.CharField(max_length=25,choices=choice2)

    def __str__(self):
        return f"({self.NAME})-({self.EMAIL_ID})"

    def get_absolute_url(self):
        return reverse('user-view')

class service(models.Model):
    # SERVICE_ID=models.IntegerField(null=True)
    SERVICE_NAME=models.CharField(max_length=25)

    def __str__(self):
        return self.SERVICE_NAME

class document(models.Model):
    # DOCUMENT_ID=models.IntegerField(null=True)
    L_ID=models.ForeignKey(user,on_delete=models.CASCADE, related_name='document')
    DOCUMENT_NAME=models.CharField(max_length=20)
    DOCUMENT_FILE=models.FileField(default="",upload_to="profile")
    SERVICE_ID=models.ForeignKey(service,on_delete=models.CASCADE, related_name='document')

    def __str__(self):
        return self.L_ID, self.SERVICE_ID

class service_detail(models.Model):
    # SD_ID=models.IntegerField(null=True)
    SERVICE_ID=models.ForeignKey(service,on_delete=models.CASCADE, related_name='service_detail')
    SERVICE_DETAIL_NAME=models.CharField(max_length=25)

    def __str__(self):
        return self.SERVICE_ID

class master_question(models.Model):
    # QUESTION_ID=models.IntegerField(null=True)
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    SD_ID=models.ForeignKey(service_detail,on_delete=models.CASCADE, related_name='master_question')

    def __str__(self):
        return self.SD_ID

class sub_question(models.Model):
    # SUB_QUESTION_ID=models.IntegerField(null=True)
    QUESTION_ID=models.ForeignKey(master_question,on_delete=models.CASCADE, related_name='sub_question')
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    SD_ID=models.ForeignKey(service_detail,on_delete=models.CASCADE, related_name='sub_question')

    def __str__(self):
        return self.QUESTION_ID, self.SD_ID