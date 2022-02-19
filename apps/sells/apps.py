from django.apps import AppConfig


class SellsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sells'
    
    def ready(self):
        import apps.sells.signals
