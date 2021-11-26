from django.urls import path
from users.api import auth
from .views import test


urlpatterns = [
    path('v1/register', auth.RegisterView.as_view(), name='register'),
    path('v1/userinfo', auth.UserInfoView.as_view(), name='userinfo'),
    path('v1/refresh', auth.RefreshTokenView.as_view(), name='refresh'),
    path('v1/login', auth.LoginView.as_view(), name='login'),
    path('v1/logout', auth.LogoutView.as_view(), name='logout'),
    path('v1/test', test, name='test'),
]
