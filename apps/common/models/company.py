# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# import base models from utils
from utils.core.models import TimeStampable

class Company(TimeStampable):
    name = models.CharField(max_length=64)
    is_sim_company = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class FRCPlans(TimeStampable):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.IntegerField()
    
    def __str__(self):
        return self.price