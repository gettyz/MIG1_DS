#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiView(ListView):
	model = Naviki
	context_object_name = 'naviki_list'
	success_url = reverse_lazy('anketa: Naviki')

	paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name

		context['collastname'] = 'Сервисы'
		return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiUpdate(UpdateView):
	model = Naviki
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/naviki/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_it','erem','created_it','updated_at','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiDetail(DetailView):
	model = Naviki
	context_object_name = 'naviki_one'
	success_url = '/anketa/naviki/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_it','erem','created_it','updated_at','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiCreate(CreateView):
	model = Naviki
	context_object_name = 'naviki_one'
	success_url = '/anketa/naviki/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'title'}
		context['secslovar'] = {''}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_it','erem','created_it','updated_at','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiDelete(DeleteView):
	model = Naviki
	success_url = '/anketa/naviki/'

