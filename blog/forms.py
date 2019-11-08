from  django import  forms
from django.contrib.auth.models import User


#登录表单继承forms.Form

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()