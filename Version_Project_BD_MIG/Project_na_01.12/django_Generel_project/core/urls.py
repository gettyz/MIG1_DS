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

from mysite.home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("mysite.authentication.urls")), # Auth routes - login / register

    path('car/', include('mysite.car.urls')),  # подключение приложения
    path('helicopter/', include('mysite.helicopter.urls')),  # подключение приложения
    path('anketa/', include('mysite.anketa.urls')),  # подключение приложения
    path('testik/', include('mysite.testik.urls')),  # подключение приложения

                  # Leave `Home.Urls` as last the last line
                  # Leave `Home.Urls` as last the last line НЕ УДАЛЯТЬ $ КАК БЫ СИЛЬНО НИ ХОТЕЛОСЬ
                  # удаление этой штуки влечет за собой изменение ссылок на скачивание всех файлов
    re_path("^$", include("mysite.home.urls")),


    path('<str:template_name>.html/', views.static_html, name='temp_html')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
