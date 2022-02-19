# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# import locals
from apps.common.models import Item
from apps.stocks.models import Stock

USER = get_user_model()

@receiver(post_save, sender=Item)
def add_stock_to_user(sender, instance, created, **kwargs):
    for user in USER.objects.all():
        Stock.objects.get_or_create(
            user = user,
            item = instance,
        )