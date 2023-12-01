#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.anketa.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfView(ListView):
    model = ModelProf
    context_object_name = 'modelprof_list'
    success_url = reverse_lazy('anketa: ModelProf')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModelProfView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("prof").verbose_name
        context['col2name'] = self.model._meta.get_field("navik").verbose_name
        context['col3name'] = self.model._meta.get_field("ball").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfUpdate(UpdateView):
    model = ModelProf
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/anketa/modelprof/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModelProfUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','updated_at','created_it','updated_it','edesc','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfDetail(DetailView):
    model = ModelProf
    context_object_name = 'modelprof_one'
    success_url = '/anketa/modelprof/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModelProfDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','updated_at','created_it','updated_it','edesc','erem'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfCreate(CreateView):
    model = ModelProf
    context_object_name = 'modelprof_one'
    success_url = '/anketa/modelprof/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ModelProfCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'prof','navik'}
        context['secslovar'] = {'ball'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'created_at','updated_at','created_it','updated_it','edesc','erem'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ModelProfDelete(DeleteView):
    model = ModelProf
    success_url = '/anketa/modelprof/'

