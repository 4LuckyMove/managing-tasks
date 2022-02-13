from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
    PasswordResetForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'autocomplete': 'new-password',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="retype password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat password',
            'autocomplete': 'new-password',
        }),
        strip=False,
        help_text="Enter the same password as before.",
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'autocomplete': 'username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'autocomplete': 'email',
            }),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'username', 'first_name', 'last_name', 'date_joined', )


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com',
            'autofocus': True,
        }),
    )
    password = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'autocomplete': 'current-password',
        }),
    )


class CustomUserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="old password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Old password',
        }),
    )
    new_password1 = forms.CharField(
        label="new password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New password',
            'autocomplete': 'new-password',
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="new password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat new password',
            'autocomplete': 'new-password',
        }),
    )


class CustomUserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
            'placeholder': 'name@example.com',
        })
    )


class CustomUserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="new password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New password',
            'autocomplete': 'new-password',
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="new password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat new password',
            'autocomplete': 'new-password',
        }),
    )