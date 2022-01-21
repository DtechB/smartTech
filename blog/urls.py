from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.Blog.as_view(), name='blog'),
    path('<str:cat>/', views.Blog.as_view(), name='blog'),
    path('api/<int:pk>', views.linked, name='api_linked'),
    path('api/<int:pk>/addpost', views.add_favorite_post, name='api_add_favorite'),
    path('post/<slug:post>/<int:pk>/', views.single_blog, name='post'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('search/page/<int:page>/', views.SearchList.as_view(), name='search'),
    path('__debug__/', include(debug_toolbar.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
