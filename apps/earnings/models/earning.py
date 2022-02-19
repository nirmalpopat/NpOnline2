# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# import base models from utils
from utils.core.models import TimeStampable

from apps.common.models import *

USER = get_user_model()

class Earning(TimeStampable):
    user = models.ForeignKey(
        USER, 
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item, 
        on_delete=models.CASCADE, 
    )
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    buy_price = models.FloatField()
    sold_price = models.FloatField()
    profit = models.FloatField()
    
    def __str__(self):
        return str(self.profit)