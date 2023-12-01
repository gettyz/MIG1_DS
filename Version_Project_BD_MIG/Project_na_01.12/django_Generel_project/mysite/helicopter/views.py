from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView

from mysite.helicopter.models import MyHelicopter

item_for_page =15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyHelicopterView(ListView):
	model = MyHelicopter
	context_object_name = 'myhelicopter_list'
	success_url = reverse_lazy('helicopter: MyHelicopter')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyHelicopterView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("name").verbose_name
		context['col2name'] = self.model._meta.get_field("color").verbose_name
		context['col3name'] = self.model._meta.get_field("nazn").verbose_name
		context['collastname'] = 'Сервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyHelicopterUpdate(UpdateView):
	model = MyHelicopter
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/helicopter/myhelicopter/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyHelicopterUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nazn'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','edesc','updated_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyHelicopterDetail(DetailView):
	model = MyHelicopter
	context_object_name = 'myhelicopter_one'
	success_url = '/helicopter/myhelicopter/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyHelicopterDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nazn'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','edesc','updated_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyHelicopterCreate(CreateView):
	model = MyHelicopter
	context_object_name = 'myhelicopter_one'
	success_url = '/helicopter/myhelicopter/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyHelicopterCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nazn'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','edesc','updated_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class MyHelicopterDelete(DeleteView):
	model = MyHelicopter
	success_url = '/helicopter/myhelicopter/'

