# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from crum import get_current_user

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# import base models from utils
from utils.core.models import TimeStampable

# import require models
from apps.common.models import Item, Company, FRCPlans

USER = get_user_model()

class Sells(TimeStampable):
    user = models.ForeignKey(
        USER, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    item = models.ForeignKey(
        Item, 
        on_delete = models.CASCADE
    )
    company = models.ForeignKey(
        Company, 
        on_delete= models.CASCADE, 
        blank=True, 
        null=True
    )
    frc = models.ForeignKey(
        FRCPlans, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    item_qty = models.IntegerField(
        default=1
    )
    price = models.IntegerField()
    comment = models.CharField(
        max_length=64, 
        blank=True, 
        null=True
    ) 

    def __str__(self):
        return f'{self.item.name} Sold by {self.user.username} at price of {self.price}'
    
    def save(self, *args, **kwargs):
        self.user = get_current_user()
        super(Sells, self).save(*args, **kwargs)