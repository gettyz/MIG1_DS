"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.testik.views import *
from mysite.home import views
app_name = 'testik'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('otvet/', OtvetView.as_view(), name='Otvet'),
    path('otvet/update/<int:pk>/', OtvetUpdate.as_view(), name='OtvetUpdate'),
    path('otvet/detail/<int:pk>/', OtvetDetail.as_view(), name='OtvetDetail'),
    path('otvet/create/', OtvetCreate.as_view(), name='OtvetCreate'),
    path('otvet/delete/<int:pk>/', OtvetDelete.as_view(), name='OtvetDelete'),

    path('sertif/', SertifView.as_view(), name='Sertif'),
    path('sertif/update/<int:pk>/', SertifUpdate.as_view(), name='SertifUpdate'),
    path('sertif/detail/<int:pk>/', SertifDetail.as_view(), name='SertifDetail'),
    path('sertif/create/', SertifCreate.as_view(), name='SertifCreate'),
    path('sertif/delete/<int:pk>/', SertifDelete.as_view(), name='SertifDelete'),
]
