# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# import locals
from apps.sells.models import *
from apps.earnings.models import *
from apps.stocks.models import *

USER = get_user_model()

@receiver(post_save, sender=Sells)
def add_earnings(sender, instance, created, **kwargs):
    if instance.item.is_company:
        # company = instance.company.objects.get(id = instance.company.id)
        if instance.company.is_stockable:
            stock_obj = Stock.objects.get(user = instance.user, item = instance.item)
            stock_obj.item_qty -= instance.item_qty
            stock_obj.save()
            buy_price = instance.company.buy_price
        elif instance.company.is_margin:
            buy_price = instance.price - (instance.price * instance.company.margin_percentage) / 100
        else:
            buy_price = instance.price - instance.frc.instinctive
    else:
        buy_price = 0
    Earning.objects.create(
        user = instance.user,
        item = instance.item,
        company = instance.company,
        buy_price = buy_price,
        sold_price = instance.price,
        profit = instance.price - buy_price
    )