from django.urls import path
from . import views

app_name = 'phone'
urlpatterns = [
    path('', views.index, name='phones'),
    path('phone1/', views.single_phone, name='single_phone')
]
