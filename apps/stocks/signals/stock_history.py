# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# import locals
from apps.common.models import Item
from apps.stocks.models import Stock, StockHistory

USER = get_user_model()

@receiver(post_save, sender=Stock)
def add_stockhistory(sender, instance, created, **kwargs):    
    StockHistory.objects.create(
        user_name=instance.user_name, 
        item_name=instance.item_name, 
        item_qty=instance.item_qty, 
        is_admin_updated = instance.is_admin_updated
    )
