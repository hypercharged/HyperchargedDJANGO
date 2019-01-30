from django import forms
from django.conf import settings
from .models import User

class LoginActivity(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password': forms.PasswordInput(),
    }
class CreatePost(forms.ModelForm):
	username = forms.CharField(label='Username', max_length=settings.USER_LENGTH) # <-- Temporary, since obviously we don't want people choosing new usernames everytime they post
	description = forms.CharField(label='Description', max_length=1000)
	image_url = forms.CharField(label='Description', max_length=1000)
