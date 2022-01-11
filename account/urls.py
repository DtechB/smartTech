# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'account'
# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#     #
#     path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#     #
#     path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]

urlpatterns = [
    path('', views.home, name='panel'),
    path('profile/', views.profile, name='profile'),
    path('comparison/', views.comparison, name='comparison'),
    path('favorite/', views.favorite, name='favorite'),
    path('api/<int:pk>/removephone', views.remove_comparison_phone, name='remove_phone'),
    path('api/<int:pk>/removepost', views.remove_favorite_post, name='remove_post'),
    path('contact/', views.contact, name='contact_us'),
    path('contact/sent/', views.contact_sent, name='contact_sent')
]
