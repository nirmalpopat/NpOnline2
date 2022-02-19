from django.contrib import admin

from apps.sells.models import *
# Register your models here.
class SellsAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item',
        'company',
        'frc',
        'item_qty',
        'price',
        'comment',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(Sells, SellsAdmin)