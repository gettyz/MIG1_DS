from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView

from mysite.car.models import MyCar

item_for_page =15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyCarView(ListView):
	model = MyCar
	context_object_name = 'mycar_list'
	success_url = reverse_lazy('car: MyCar')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyCarView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("name").verbose_name
		context['col2name'] = self.model._meta.get_field("color").verbose_name
		context['col3name'] = self.model._meta.get_field("nomb").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyCarUpdate(UpdateView):
	model = MyCar
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/car/mycar/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyCarUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyCarDetail(DetailView):
	model = MyCar
	context_object_name = 'mycar_one'
	success_url = '/car/mycar/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyCarDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyCarCreate(CreateView):
	model = MyCar
	context_object_name = 'mycar_one'
	success_url = '/car/mycar/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyCarCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyCarDelete(DeleteView):
	model = MyCar
	success_url = '/car/mycar/'


