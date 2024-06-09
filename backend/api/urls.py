# backend/api/urls.py

from django.urls import path
from .views import ForgotPasswordView, ResetPasswordView, VerifyResetCodeView, signin, signup, GameListView

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('verify-reset-code/', VerifyResetCodeView.as_view(), name='verify_reset_code'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('games/', GameListView.as_view(), name='game_list'),  # Ensure this endpoint exists
]