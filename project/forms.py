from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'bio', 'phone_number', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['name', 'bio', 'phone_number', 'location', 'image']:
            self.fields[fieldname].help_text = None


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['category', 'title', 'body', 'image']


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['category', 'title', 'body', 'image']


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'button-addon2',
        'placeholder': 'write your comments here....'
    }))

    class Meta:
        model = CommentModel
        fields = ['body']

