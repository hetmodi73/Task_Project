from django.db import models
from django.urls import reverse
# Create your models here.

class contact(models.Model):
    # CONTACT_ID=models.IntegerField(null=True)
    NAME=models.CharField(max_length=25)
    EMAIL=models.EmailField(max_length=25)
    NUMBER=models.IntegerField()
    MESSAGE=models.TextField(max_length=25)

    def __str__(self):
        return self.EMAIL

    def get_absolute_url(self):
        return reverse('contact-view')
