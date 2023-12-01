from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.models import User, Group


def cfg_assets_root(request):

    if request.user.is_authenticated:
        # Получаем объект группы пользователя из таблицы auth_user_groups
        user_group = Group.objects.filter(user=request.user).first()

        if user_group and user_group.name == "управляющие":
        # if request.user.is_superuser:
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
                {
                    'name': 'пакет 3',
                    'color': 'text-warning',
                    'children': [
                        {'name': 'Навыки', 'url': reverse('anketa:Naviki')},
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

