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

USER = get_user_model()

class StockHistory(TimeStampable):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    item_qty = models.IntegerField()
    is_admin_updated = models.BooleanField(editable=False)
    
    def __str__(self):
        return f'{self.user.username} has {self.item_qty} {self.item.name}'