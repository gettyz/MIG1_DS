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

class MyCar(Forlog):
    name = models.CharField(max_length=255, blank=False, null= False, default="Машинка", verbose_name="Название")
    color = models.CharField(max_length=255, blank=False, null = False, default="Черный", verbose_name="Цвет")
    nomb = models.CharField(max_length=255, blank=False, null = False, default="TO123P", verbose_name="Номер")

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Машинка'
        verbose_name_plural = 'Машинки'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('car', kwargs={"slug": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MyCar._meta.fields]