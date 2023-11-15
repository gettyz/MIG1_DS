from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Proffessia(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Профессия")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Proffessia._meta.fields]


class Naviki(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Навыки")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Naviki._meta.fields]


class Sertifikat(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Тип")
    polniy = models.FileField(max_length=255, verbose_name="Сертификат")


    class Meta:
        ordering = ["-title"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Sertifikat._meta.fields]


class Voprosi(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вопросы")
    ball = models.IntegerField(blank=True, null=True, default='0', verbose_name="Баллы")
    navik = models.ForeignKey(Naviki, on_delete=models.PROTECT, verbose_name="Навык")


    class Meta:
        ordering = ["-title"]
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Voprosi._meta.fields]

class Grazhdanin(User):
    avatar = models.ImageField(max_length=100, verbose_name="Аватар")
    nomer = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер Телефона")
    sertific = models.FileField(max_length=255, verbose_name="Сертификат")


    class Meta:
        ordering = ["-id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Grazhdanin._meta.fields]

class ModelProf(models.Model):
    prof = models.ForeignKey(Grazhdanin, on_delete=models.PROTECT, verbose_name="Пользователь")
    navik = models.ForeignKey(Naviki, on_delete=models.PROTECT, verbose_name="Навык")
    ball = models.IntegerField(blank=True, null=True, default='0', verbose_name="Баллы")

    class Meta:
        ordering = ["-navik"]
        verbose_name = "Модельная профессия"
        verbose_name_plural = "Модельные профессии"

    def __str__(self):
        return str(self.ball)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ModelProf._meta.fields]

