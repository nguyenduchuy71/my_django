from django.urls import path
from .views import RegisterView, CustomLoginView, profile, logout_view, ResetPasswordView, ChangePasswordView
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('resetpassword/', ResetPasswordView.as_view(), name='resetpassword'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
