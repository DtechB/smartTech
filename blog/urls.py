from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post1/', views.single_blog, name='post'),
    path('__debug__/', include(debug_toolbar.urls))
]
