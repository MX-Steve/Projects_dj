from django.urls import path

from . import views

urlpatterns = [
    path('v1/login', views.login_view, name='login'),
    path('v1/logout', views.logout_view, name='logout'),
]
