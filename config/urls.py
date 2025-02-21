"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings 
from core.views import index, sign_up, numbers
from blog.views import *
from playlist.views import playlist, add_video


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('sign_up/', sign_up),
    path('numbers/', numbers),
    path('blog/', blog),
    path('playlist/', playlist, name='playlist'),
    path('add_video', add_video, name='add_video')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
