from django import forms
from .models import Contacts, Reviews

class ContactsForm(forms.ModelForm):
    class Meta: 
        model = Contacts
        fields = ['contact_name', 'contact_email', 'message']

class ReviewsForm(forms.ModelForm):
    class Meta: 
        model = Reviews
        fields = ['product_id', 'customer_name', 'customer_email', 'review', 'rate']