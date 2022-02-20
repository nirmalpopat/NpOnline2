from crum import get_current_user

from django.db import models

class ByAgent(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            user=get_current_user()
        ).order_by('-create_date')