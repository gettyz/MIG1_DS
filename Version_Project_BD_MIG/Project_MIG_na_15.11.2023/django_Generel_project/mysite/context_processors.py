from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


def cfg_assets_root(request):

    if request.user.is_authenticated:
        if request.user.is_superuser:
            sidebar = [

                {
                    'name': 'пакет 1',
                    'color': 'text-danger',
                     'children': [
                         {'name': 'Машинки', 'url': reverse('car:MyCar')},
                    ]
                },
                {
                    'name': 'пакет 2',
                    'color': 'text-warning',
                    'children': [
                        {'name': 'Вертолеты', 'url': reverse('helicopter:MyHelicopter')},
                    ]
                },
            ]
        else: sidebar = [{
            'name': 'пакет 2',
            'color': 'text-warning',
            'children': [
                {'name': 'Вертолеты', 'url': reverse('helicopter:MyHelicopter')},
            ]
            }]
    else: sidebar = []

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT, 'SIDEBAR':  sidebar}

