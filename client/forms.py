from django import forms
from client.models import Signup
class Signupform(forms.ModelForm):
    class Meta:
        model = Signup
        widgets={
            'password': forms.PasswordInput()
        }