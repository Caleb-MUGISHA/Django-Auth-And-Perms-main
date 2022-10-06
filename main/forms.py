from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

ROLES= (
    ('Student','Student'),
    ('Facilitator','Facilitator'),
    ('Team Lead','Team Lead'),
   
    )
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role=forms.ChoiceField(choices=ROLES)

    class Meta:
        model = User
        fields = ["username", "email", "role","password1", "password2"]
        
       
       


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
