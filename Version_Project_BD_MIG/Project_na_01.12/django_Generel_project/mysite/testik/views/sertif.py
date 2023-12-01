#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from mysite.testik.models import *
item_for_page = 15

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifView(ListView):
    model = Sertif
    context_object_name = 'sertif_list'
    success_url = reverse_lazy('testik: Sertif')

    paginate_by = item_for_page
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifView,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name_plural
        context['col1name'] = self.model._meta.get_field("sertif").verbose_name
        context['col2name'] = self.model._meta.get_field("polzovatel").verbose_name
        context['col3name'] = self.model._meta.get_field("osnnavik").verbose_name
        context['col4name'] = self.model._meta.get_field("vsenavik").verbose_name
        context['col5name'] = self.model._meta.get_field("data").verbose_name
        context['col6name'] = self.model._meta.get_field("itog").verbose_name

        context['collastname'] = 'Сервисы'
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifUpdate(UpdateView):
    model = Sertif
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/testik/sertif/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifUpdate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'polzovatel','osnnavik','sertif'}
        context['secslovar'] = {'data','vsenavik','itog'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','created_at','created_it','erem','updated_at','updated_it'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDetail(DetailView):
    model = Sertif
    context_object_name = 'sertif_one'
    success_url = '/testik/sertif/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifDetail,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['slovar'] = {'polzovatel','osnnavik','sertif'}
        context['secslovar'] = {'data','vsenavik','itog'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','created_at','created_it','erem','updated_at','updated_it'}
        context['model'] = self.model
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifCreate(CreateView):
    model = Sertif
    context_object_name = 'sertif_one'
    success_url = '/testik/sertif/'

    template_name_suffix = '_create_form'
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SertifCreate,self).get_context_data(**kwargs)
        context['sometry'] = self.model._meta.verbose_name
        context['model'] = self.model
        context['slovar'] = {'polzovatel','osnnavik','sertif'}
        context['secslovar'] = {'data','vsenavik','itog'}
        context['hidenslovar'] = {'id'}
        context['dopslovar'] = {'edesc','created_at','created_it','erem','updated_at','updated_it'}
        return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SertifDelete(DeleteView):
    model = Sertif
    success_url = '/testik/sertif/'

