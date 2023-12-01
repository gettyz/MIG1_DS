from django.contrib import admin

from mysite.helicopter.models import MyHelicopter


# Register your models here.

class MyHelicopterAdmin(admin.ModelAdmin):
	ttt = ('id', 'name','color','nazn')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(MyHelicopter, MyHelicopterAdmin)