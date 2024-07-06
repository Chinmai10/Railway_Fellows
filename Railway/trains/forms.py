from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username','email','password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','email','password']


class NumberForm(forms.Form):
    number_book = forms.IntegerField(max_value=100)