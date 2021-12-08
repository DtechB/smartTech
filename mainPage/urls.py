from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page-index'),
    path('login/', views.login, name='main-page-login'),
    path('register/', views.register, name='main-page-register'),
    path('login/forgot-password/', views.forgot, name='main-page-forgot-pass')
]
