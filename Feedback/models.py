from django.db import models
from client.models import user
from django.urls import reverse
# Create your models here.

class feedback(models.Model):
    # FEED_ID=models.IntegerField(null=True)
    client=models.ForeignKey(user,on_delete=models.CASCADE, related_name='feedback')
    RATINGS=models.CharField(max_length=25)
    COMMENT=models.CharField(max_length=25)

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse('feedback-view')
