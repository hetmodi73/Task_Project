from django.contrib import admin
from .models import feedback
# Register your models here.

class showfeedback(admin.ModelAdmin):
    list_display = ['client','RATINGS','COMMENT']

admin.site.register(feedback,showfeedback)
