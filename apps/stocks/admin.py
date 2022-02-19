from django.contrib import admin

from apps.stocks.models import *
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item',
        'item_qty',
        'is_admin_updated',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(Stock, StockAdmin)

class StockHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item',
        'item_qty',
        'is_admin_updated',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(StockHistory, StockHistoryAdmin)