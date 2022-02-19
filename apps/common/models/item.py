# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# import base models from utils
from utils.core.models import TimeStampable

class Item(TimeStampable):
    name = models.CharField(max_length=64, unique=True)
    price = models.IntegerField(default=0)
    is_stockable = models.BooleanField()