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

from mysite.helicopter.views import *
from mysite.home import views
app_name = 'helicopter'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('myhelicopter/', MyHelicopterView.as_view(), name='MyHelicopter'),
    path('myhelicopter/update/<int:pk>/', MyHelicopterUpdate.as_view(), name='MyHelicopterUpdate'),
    path('myhelicopter/detail/<int:pk>/', MyHelicopterDetail.as_view(), name='MyHelicopterDetail'),
    path('myhelicopter/create/', MyHelicopterCreate.as_view(), name='MyHelicopterCreate'),
    path('myhelicopter/delete/<int:pk>/', MyHelicopterDelete.as_view(), name='MyHelicopterDelete'),
]
