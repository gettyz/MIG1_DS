from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Forlog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    edesc = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    erem = models.BooleanField(default=False, verbose_name='Удалить?')

    class Meta:
        abstract = True

###########################################################################################


class MyHelicopter(Forlog):
    name = models.CharField(max_length=255, blank=False, null= False, default="Валера23", verbose_name="Модель")
    color = models.CharField(max_length=255, blank=False, null = False, default="Черный", verbose_name="Цвет")
    nazn = models.CharField(max_length=255, blank=False, null = False, default="Спасатель", verbose_name="Назначение")

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Вертолет'
        verbose_name_plural = 'Вертолеты'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('helicopter', kwargs={"slug": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MyHelicopter._meta.fields]