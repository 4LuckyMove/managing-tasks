from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import (
    SignUpView,
    CustomUserLoginView,
    CustomUserLogoutView,
    CustomUserPasswordChangeView,
    CustomUserPasswordChangeDoneView,
    CustomUserPasswordResetView,
    CustomUserPasswordResetDoneView,
    CustomUserPasswordResetConfirmView,
    CustomUserPasswordResetCompleteView,
)

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),

    path('password_change/', CustomUserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', CustomUserPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', CustomUserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomUserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomUserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomUserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)