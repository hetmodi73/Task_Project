from django.contrib import admin
from .models import document,master_question,sub_question
# Register your models here.

class showdocument(admin.ModelAdmin):
    list_display = ['client','DOCUMENT_NAME','DOCUMENT_FILE','services']

admin.site.register(document,showdocument)

class showmaster_question(admin.ModelAdmin):
    list_display = ['QUESTION','ANSWER','POINTS','services']

admin.site.register(master_question,showmaster_question)

class showsub_question(admin.ModelAdmin):
    list_display = ['QUESTION_ID','QUESTION','ANSWER','POINTS','services']

admin.site.register(sub_question,showsub_question)
