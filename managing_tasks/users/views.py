from django.contrib.auth import views, REDIRECT_FIELD_NAME
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    CustomUserCreationForm,
    CustomUserAuthenticationForm,
    CustomUserPasswordChangeForm,
    CustomUserPasswordResetForm,
    CustomUserPasswordResetConfirmForm,
)


class CustomUserLoginView(views.LoginView):
    form_class = CustomUserAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomUserLogoutView(views.LogoutView):
    redirect_field_name = REDIRECT_FIELD_NAME


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomUserPasswordChangeView(views.PasswordChangeView):
    form_class = CustomUserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'


class CustomUserPasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class CustomUserPasswordResetView(views.PasswordResetView):
    form_class = CustomUserPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'


class CustomUserPasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomUserPasswordResetConfirmView(views.PasswordResetConfirmView):
    form_class = CustomUserPasswordResetConfirmForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'registration/password_reset_confirm.html'


class CustomUserPasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
