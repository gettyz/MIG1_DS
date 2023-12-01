"""
URL configuration for core project.
#!/usr/bin/env python
# -*- coding: utf8 -*-
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

from mysite.anketa.views import *
from mysite.home import views
app_name = 'anketa'
urlpatterns = [
    #path('admin/', admin.site.urls),

    path('proffessia/', ProffessiaView.as_view(), name='Proffessia'),
    path('proffessia/update/<int:pk>/', ProffessiaUpdate.as_view(), name='ProffessiaUpdate'),
    path('proffessia/detail/<int:pk>/', ProffessiaDetail.as_view(), name='ProffessiaDetail'),
    path('proffessia/create/', ProffessiaCreate.as_view(), name='ProffessiaCreate'),
    path('proffessia/delete/<int:pk>/', ProffessiaDelete.as_view(), name='ProffessiaDelete'),

    path('naviki/', NavikiView.as_view(), name='Naviki'),
    path('naviki/update/<int:pk>/', NavikiUpdate.as_view(), name='NavikiUpdate'),
    path('naviki/detail/<int:pk>/', NavikiDetail.as_view(), name='NavikiDetail'),
    path('naviki/create/', NavikiCreate.as_view(), name='NavikiCreate'),
    path('naviki/delete/<int:pk>/', NavikiDelete.as_view(), name='NavikiDelete'),

    path('sertifikat/', SertifikatView.as_view(), name='Sertifikat'),
    path('sertifikat/update/<int:pk>/', SertifikatUpdate.as_view(), name='SertifikatUpdate'),
    path('sertifikat/detail/<int:pk>/', SertifikatDetail.as_view(), name='SertifikatDetail'),
    path('sertifikat/create/', SertifikatCreate.as_view(), name='SertifikatCreate'),
    path('sertifikat/delete/<int:pk>/', SertifikatDelete.as_view(), name='SertifikatDelete'),

    path('voprosi/', VoprosiView.as_view(), name='Voprosi'),
    path('voprosi/update/<int:pk>/', VoprosiUpdate.as_view(), name='VoprosiUpdate'),
    path('voprosi/detail/<int:pk>/', VoprosiDetail.as_view(), name='VoprosiDetail'),
    path('voprosi/create/', VoprosiCreate.as_view(), name='VoprosiCreate'),
    path('voprosi/delete/<int:pk>/', VoprosiDelete.as_view(), name='VoprosiDelete'),

    path('grazhdanin/', GrazhdaninView.as_view(), name='Grazhdanin'),
    path('grazhdanin/update/<int:pk>/', GrazhdaninUpdate.as_view(), name='GrazhdaninUpdate'),
    path('grazhdanin/detail/<int:pk>/', GrazhdaninDetail.as_view(), name='GrazhdaninDetail'),
    path('grazhdanin/create/', GrazhdaninCreate.as_view(), name='GrazhdaninCreate'),
    path('grazhdanin/delete/<int:pk>/', GrazhdaninDelete.as_view(), name='GrazhdaninDelete'),

    path('modelprof/', ModelProfView.as_view(), name='ModelProf'),
    path('modelprof/update/<int:pk>/', ModelProfUpdate.as_view(), name='ModelProfUpdate'),
    path('modelprof/detail/<int:pk>/', ModelProfDetail.as_view(), name='ModelProfDetail'),
    path('modelprof/create/', ModelProfCreate.as_view(), name='ModelProfCreate'),
    path('modelprof/delete/<int:pk>/', ModelProfDelete.as_view(), name='ModelProfDelete'),
]
