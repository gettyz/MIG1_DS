#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaView(ListView):
	model = Proffessia
	context_object_name = 'proffessia_list'
	success_url = reverse_lazy('anketa: Proffessia')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name

		context['collastname'] = 'Сервисы'
		return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaUpdate(UpdateView):
	model = Proffessia
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/proffessia/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','updated_at','updated_it','edesc','created_it'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaDetail(DetailView):
	model = Proffessia
	context_object_name = 'proffessia_one'
	success_url = '/anketa/proffessia/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','updated_at','updated_it','edesc','created_it'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaCreate(CreateView):
	model = Proffessia
	context_object_name = 'proffessia_one'
	success_url = '/anketa/proffessia/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'created_at','erem','updated_at','updated_it','edesc','created_it'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaDelete(DeleteView):
	model = Proffessia
	success_url = '/anketa/proffessia/'