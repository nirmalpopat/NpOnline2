from django.contrib import admin

from apps.common.models import * 
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(Company, CompanyAdmin)

class FRCPlansAdmin(admin.ModelAdmin):
    list_display = [
        'company',
        'price',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(FRCPlans, FRCPlansAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_stockable',
        'create_date',
        'modified_date',
    ]
    
admin.site.register(Item, ItemAdmin)