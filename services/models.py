from django.db import models
from django.urls import reverse
# Create your models here.

class service(models.Model):
    # SERVICE_ID=models.IntegerField(null=True)
    SERVICE_NAME=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.SERVICE_NAME}"

    def get_absolute_url(self):
        return reverse('service-view')

class service_details(models.Model):
    # SD_ID=models.IntegerField(null=True)
    SERVICE_ID=models.ForeignKey(service,on_delete=models.CASCADE, related_name='service_detail', blank=True,null=True)
    SERVICE_DETAIL_NAME=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.SERVICE_ID}-{self.SERVICE_DETAIL_NAME}"

    def get_absolute_url(self):
        return reverse('service_details-view')


