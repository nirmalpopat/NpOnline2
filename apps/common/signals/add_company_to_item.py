# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# import locals
from apps.common.models import Item, Company
from apps.stocks.models import Stock

USER = get_user_model()

@receiver(post_save, sender=Company)
def add_company_to_item(sender, instance, created, **kwargs):
    Item.objects.get(
        id = instance.item.id,
    ).company.add(
        instance
    )