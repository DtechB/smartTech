from django.urls import path
from . import views

app_name = 'phone'
urlpatterns = [
    path('api/<int:pk>', views.link, name='api_link'),
    path('api/<int:pk>/addphone', views.add_comparison_phone, name='api_add_comparison'),
    path('', views.index, name='phones'),
    path('phone/<slug:phone>/<int:pk>/', views.single_phone, name='single_phone')
]
