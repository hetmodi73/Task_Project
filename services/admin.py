from django.contrib import admin
from .models import service,service_details
# Register your models here.

class showservice(admin.ModelAdmin):
    list_display = ['SERVICE_NAME']

admin.site.register(service,showservice)

class showservice_details(admin.ModelAdmin):
    list_display = ['SERVICE_ID','SERVICE_DETAIL_NAME']

admin.site.register(service_details,showservice_details)
