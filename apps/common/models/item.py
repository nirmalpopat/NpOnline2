# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# import base models from utils
from utils.core.models import TimeStampable

USER = get_user_model()

class Item(TimeStampable):
    name = models.CharField(max_length=64, unique=True)
    price = models.IntegerField(default=0)
    is_stockable = models.BooleanField()
    
class Company(TimeStampable):
    name = models.CharField(max_length=64)
    is_sim_company = models.BooleanField()
    
class FRCPlans(TimeStampable):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)