from django.contrib import admin
from.models import login,user, Signup
# Register your models here.

class showlogin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(login,showlogin)

class showuser(admin.ModelAdmin):
    list_display = ['EMAIL_ID','PHONE_NO','PASSWORD','NAME','GENDER','ADDRESS','ROLE','STATUS']

admin.site.register(user,showuser)

class showSignup(admin.ModelAdmin):
    list_display = ['name','email','password','re_pass']

admin.site.register(Signup,showSignup)
