from django.forms import ModelForm
from django.core import validators
from .models import login
from django import forms

class SignIn(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"


#class Signup(forms.ModelForm):
#    class Meta:
#        model=Signup
#        fields="__all__"

#class Loginn(forms.ModelForm):
#    class Meta:
#        model=Loginn
#        fields="__all__"

#class Login(forms.Form):
 #   username=forms.CharField(label="Username")
  #  email=forms.EmailField(max_length=40)
   # password=forms.CharField(widget=forms.PasswordInput)

   #class Singnup(forms.Form):
       #first_name=forms.CharField(label="FirstName", validators=[check])
       #last_name=forms.CharField(label="LastName")
       #password=forms.CharField(widget=forms.PasswordInput)
       #verify_password=forms.CharField(widget=forms.PasswordInput)
    