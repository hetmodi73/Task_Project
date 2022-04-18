from django.db import models
from django.urls import reverse

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}-{self.password}"

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
        return f"{self.NAME}-{self.EMAIL_ID}"

    def get_absolute_url(self):
        return reverse('user-view')

class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    re_pass=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}-{self.email}"

    def get_absolute_url(self):
        return reverse('index')




