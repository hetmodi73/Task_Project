from django.contrib import admin
from.models import user
# Register your models here.

class showuser(admin.ModelAdmin):
    list_display = ['EMAIL_ID','PHONE_NO','PASSWORD','NAME','GENDER','ADDRESS','ROLE','STATUS']

admin.site.register(user,showuser)
