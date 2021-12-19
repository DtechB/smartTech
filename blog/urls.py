from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post>/<int:pk>', views.single_blog, name='post'),
    path('__debug__/', include(debug_toolbar.urls))
]
