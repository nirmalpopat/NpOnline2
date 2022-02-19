# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# import base models from utils
from utils.core.models import TimeStampable

# import require models
from apps.common.models.item import Item
from apps.common.models.company import Company, FRCPlans

USER = get_user_model()

class Sells(TimeStampable):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete= models.CASCADE, default="", blank=True, null=True)
    frc = models.ForeignKey(FRCPlans, on_delete=models.CASCADE)
    item_qty = models.IntegerField(default=1)
    price = models.IntegerField()
    comment = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return f'{self.item_name.name} Sold by {self.user.username} at price of {self.price}'