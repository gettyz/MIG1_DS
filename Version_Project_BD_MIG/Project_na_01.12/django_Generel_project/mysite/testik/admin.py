from django.contrib import admin

from mysite.testik.models import *


# Register your models here.

class OtvetAdmin(admin.ModelAdmin):
	ttt = ('id', 'polzovatel', 'navik', 'ball', 'data')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Otvet, OtvetAdmin)


class SertifAdmin(admin.ModelAdmin):
	ttt = ('id', 'sertif', 'polzovatel', 'osnnavik', 'vsenavik', 'data', 'itog')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Sertif, SertifAdmin)