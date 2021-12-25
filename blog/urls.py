from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<slug:post>/<int:pk>/', views.single_blog, name='post'),
    path('__debug__/', include(debug_toolbar.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
