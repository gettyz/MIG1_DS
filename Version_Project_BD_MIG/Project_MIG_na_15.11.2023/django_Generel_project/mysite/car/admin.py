from django.contrib import admin

from mysite.car.models import MyCar


# Register your models here.

class MyCarAdmin(admin.ModelAdmin):
	ttt = ('id', 'name','color','nomb')
	list_display = ttt
	list_display_links = ttt
	search_fields = ttt

admin.site.register(MyCar, MyCarAdmin)