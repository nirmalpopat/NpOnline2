# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# import base models from utils
from utils.core.models import TimeStampable



class Item(TimeStampable):
    name = models.CharField(
        max_length=64, 
        unique=True
    )
    is_company = models.BooleanField(default=True)
    company = models.ManyToManyField(
        'Company', 
        blank=True, 
        null=True, 
        related_name = 'item_company'
    )
    is_stockable = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Company(TimeStampable):
    item = models.ForeignKey(
        Item, 
        on_delete = models.CASCADE, 
        related_name = 'company_item'
    )
    name = models.CharField(
        max_length=64
    )
    is_stockable = models.BooleanField()
    buy_price = models.FloatField(
        blank=True, 
        null=True
    )
    is_margin = models.BooleanField(default=False)
    margin_percentage = models.FloatField(
        blank=True,
        null=True
    )
    frc_plans = models.ManyToManyField(
        'FRCPlans',
        blank=True,
        null=True,
        related_name = 'company_frc_plans'
    )
    
    def __str__(self):
        return f'{self.name} {self.item.name}'
    
class FRCPlans(TimeStampable):
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name = 'frc_plans_company'
    )
    price = models.IntegerField()
    validity = models.CharField(
        max_length=64
    )
    instinctive = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.company.name} {str(self.price)}'