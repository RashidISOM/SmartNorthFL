
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Food


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
      model = User
      fields = ["username", "email", "password1", "password2"]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Name', 'Status', 'Amount')

