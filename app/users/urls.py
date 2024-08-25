from django.urls import path

from .views import CreateUserView, LoginUserView, AuthTokenView, EmailConfirmationView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('auth/', AuthTokenView.as_view(), name='auth_token'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='email_confirmation'),
]
