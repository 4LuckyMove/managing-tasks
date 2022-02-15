from django import forms
from django.contrib.auth import get_user_model

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description',
                    'style': 'height: 150px;',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                },
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'name@example.com',
                    'autocomplete': 'email',
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First Name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last Name',
                },
            ),
        }
