# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import pytz
import datetime

# lib imports
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http.response import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# local imports 
from apps.sells.models.sell import Sells
from apps.sells.forms import SellsForm

# Create your views here.

class AddSellView(LoginRequiredMixin, View):   
    template_name = 'sells/AddSell.html'
    form_class = SellsForm
    
    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.form_class
        context['report'] = Sells.byAgent.all()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        
        if self.form_class(request.POST).is_valid():
            self.form_class(request.POST).save()
        context = {}
        context['form'] = self.form_class
        context['report'] = Sells.byAgent.all()
        return render(request, self.template_name, context)
