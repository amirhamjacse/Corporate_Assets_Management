from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True
    )
    is_active = models.BooleanField(
        _('Is Active'), default=True
    )

    class Meta:
        abstract = True