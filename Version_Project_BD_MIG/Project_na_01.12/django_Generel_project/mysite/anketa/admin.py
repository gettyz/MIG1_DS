from django.contrib import admin

from mysite.anketa.models import *


# Register your models here.

class ProffessiaAdmin(admin.ModelAdmin):
	ttt = ('id', 'title')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Proffessia, ProffessiaAdmin)

class NavikiAdmin(admin.ModelAdmin):
	ttt = ('id', 'title')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Naviki, NavikiAdmin)

class SertifikatAdmin(admin.ModelAdmin):
	ttt = ('id', 'title', 'polniy')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Sertifikat, SertifikatAdmin)

class VoprosiAdmin(admin.ModelAdmin):
	ttt = ('id', 'title', 'ball', 'navik')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Voprosi, VoprosiAdmin)


class GrazhdaninAdmin(admin.ModelAdmin):
	ttt = ('id', 'avatar', 'nomer', 'sertific')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(Grazhdanin, GrazhdaninAdmin)

class ModelProfAdmin(admin.ModelAdmin):
	ttt = ('id', 'prof', 'navik', 'ball')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(ModelProf, ModelProfAdmin)