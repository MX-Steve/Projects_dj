from django.urls import path
from users.api import auth
from . import views


urlpatterns = [
    path('v1/login', auth.login_view, name='login'),
    path('v1/logout', auth.logout_view, name='logout'),
    path('v1/test', views.test),
]
