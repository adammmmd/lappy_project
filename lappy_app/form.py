from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacts, Reviews

class ContactsForm(forms.ModelForm):
    class Meta: 
        model = Contacts
        fields = ['contact_name', 'contact_email', 'message']

class ReviewsForm(forms.ModelForm):
    class Meta: 
        model = Reviews
        fields = ['product_id', 'customer_name', 'customer_email', 'review', 'rate']

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)