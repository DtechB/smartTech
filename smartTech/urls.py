"""smartTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from account.views import signup, activate

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', signup, name='register'),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', include('mainPage.urls')),
    path('', include('django.contrib.auth.urls')),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('blog/', include('blog.urls')),
    path('smartphones/', include('phone.urls')),
    path('account/', include('account.urls')),
    path('summernote/', include('django_summernote.urls'))
]

handler404 = 'mainPage.views.not_found_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
