from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post1/', views.single_blog, name='post')
]
