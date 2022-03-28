from django.contrib import admin
from .models import contact
# Register your models here.

class showcontact(admin.ModelAdmin):
    list_display = ['NAME','EMAIL','NUMBER','MESSAGE']

admin.site.register(contact,showcontact)
