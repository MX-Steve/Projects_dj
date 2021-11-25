from django.urls import path
from users.api import auth


urlpatterns = [
    path('v1/login', auth.LoginView.as_view(), name='login'),
    path('v1/logout', auth.LogoutView.as_view(), name='logout'),
]
