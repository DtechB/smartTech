from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.index, name='main-page-index'),
    path('register/', views.register, name='main-page-register'),
    path('login/forgot-password/', views.forgot, name='main-page-forgot-pass')
]
