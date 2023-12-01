#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class GrazhdaninView(ListView):
    model = Grazhdanin
    context_object_name = 'grazhdanin_list'
    success_url = reverse_lazy('anketa: Grazhdanin')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GrazhdaninView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("avatar").verbose_name
        context['col2name'] = self.model._meta.get_field("nomer").verbose_name
        context['col3name'] = self.model._meta.get_field("sertific").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class GrazhdaninUpdate(UpdateView):
    model = Grazhdanin
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/anketa/grazhdanin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GrazhdaninUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'avatar','nomer'}
        context['secslovar'] = {'sertific'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','edesc','created_it','updated_it','erem','updated_at'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class GrazhdaninDetail(DetailView):
    model = Grazhdanin
    context_object_name = 'grazhdanin_one'
    success_url = '/anketa/grazhdanin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GrazhdaninDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'avatar','nomer'}
        context['secslovar'] = {'sertific'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','edesc','created_it','updated_it','erem','updated_at'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class GrazhdaninCreate(CreateView):
    model = Grazhdanin
    context_object_name = 'grazhdanin_one'
    success_url = '/anketa/grazhdanin/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GrazhdaninCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'avatar','nomer'}
        context['secslovar'] = {'sertific'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','edesc','created_it','updated_it','erem','updated_at'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class GrazhdaninDelete(DeleteView):
    model = Grazhdanin
    success_url = '/anketa/grazhdanin/'

