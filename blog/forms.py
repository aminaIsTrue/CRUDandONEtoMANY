from django import forms
from django.contrib.auth.models import User

from .models import Post, Contribution

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class ContributionForm(forms.ModelForm):
    
    class Meta:
        model = Contribution
        fields = ['user','contribution']