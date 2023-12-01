#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.testik.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class OtvetView(ListView):
    model = Otvet
    context_object_name = 'otvet_list'
    success_url = reverse_lazy('testik: Otvet')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OtvetView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("polzovatel").verbose_name
        context['col2name'] = self.model._meta.get_field("navik").verbose_name
        context['col3name'] = self.model._meta.get_field("ball").verbose_name
        context['col4name'] = self.model._meta.get_field("data").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class OtvetUpdate(UpdateView):
    model = Otvet
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/testik/otvet/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OtvetUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball','data'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','updated_at','updated_it','created_it','created_at','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class OtvetDetail(DetailView):
    model = Otvet
    context_object_name = 'otvet_one'
    success_url = '/testik/otvet/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OtvetDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball','data'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','updated_at','updated_it','created_it','created_at','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class OtvetCreate(CreateView):
    model = Otvet
    context_object_name = 'otvet_one'
    success_url = '/testik/otvet/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OtvetCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball','data'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','updated_at','updated_it','created_it','created_at','erem'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class OtvetDelete(DeleteView):
    model = Otvet
    success_url = '/testik/otvet/'

