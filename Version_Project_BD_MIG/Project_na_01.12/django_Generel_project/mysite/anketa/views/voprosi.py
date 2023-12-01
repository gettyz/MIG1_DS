#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosiView(ListView):
    model = Voprosi
    context_object_name = 'voprosi_list'
    success_url = reverse_lazy('anketa: Voprosi')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VoprosiView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("title").verbose_name
        context['col2name'] = self.model._meta.get_field("ball").verbose_name
        context['col3name'] = self.model._meta.get_field("navik").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosiUpdate(UpdateView):
    model = Voprosi
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/anketa/voprosi/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VoprosiUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'ball','title'}
        context['secslovar'] = {'navik'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_it','edesc','updated_it','created_at','updated_at','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosiDetail(DetailView):
    model = Voprosi
    context_object_name = 'voprosi_one'
    success_url = '/anketa/voprosi/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VoprosiDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'ball','title'}
        context['secslovar'] = {'navik'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_it','edesc','updated_it','created_at','updated_at','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosiCreate(CreateView):
    model = Voprosi
    context_object_name = 'voprosii_one'
    success_url = '/anketa/voprosi/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VoprosiCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'ball','title'}
        context['secslovar'] = {'navik'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_it','edesc','updated_it','created_at','updated_at','erem'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosiDelete(DeleteView):
    model = Voprosi
    success_url = '/anketa/voprosi/'

