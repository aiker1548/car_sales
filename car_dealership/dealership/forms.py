from django import forms
from .models import ContactMessage, Request
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2') 

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'message']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['car', 'request_type']
