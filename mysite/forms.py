
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
      model = User
      fields = ["username", "email", "password1", "password2"]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Name', 'Status', 'Amount')
        
class mailForm(forms.Form):
    Subject = forms.CharField()
    Message =forms.CharField(widget=forms.Textarea)

class findPantry(forms.ModelForm):
    class Meta:
      model = Location
      fields = ('zipCode',)
class PantryForm(forms.ModelForm):
    class Meta:
        model = Pantry
        fields = ('name', 'zipCode', 'streetAdd1', 'streetAdd2', 'city', 'state', 'phone_number', 'websiteURL', 'description')

class donorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'pantry', 'email')
class TimeInput(forms.TimeInput):
    input_type = "time"

class HoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ('weekday', 'from_hour', 'to_hour')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["from_hour"].widget = TimeInput()
        self.fields["to_hour"].widget = TimeInput()
        self.fields["weekday"]
class NeedForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = ('itemName',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['itemName'].label = "Item Name"
