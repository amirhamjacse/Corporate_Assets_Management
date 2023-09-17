from django.db import models
from django.contrib.auth.models import User
from corporate_assets_management.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _

class EmployeeInfo(AbstractBaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    company_info = models.ForeignKey(
        "CompanyInfo", on_delete=models.CASCADE,
        related_name='company_inf'
    )
    device_info = models.ManyToManyField(
        "DevicesInfo", related_name='devices_informations'
    )


class CompanyInfo(AbstractBaseModel):
    name = models.CharField(
        _('Company Name'),
        max_length=255, blank=True,
    )
    address = models.CharField(
        _('Company Address'),
        max_length=255, blank=True, null=True
    )
    mobile_number = models.CharField(
        _('Company Mobile Number'),
        max_length=12, unique=True,
        null=True, blank=True
    )
    website = models.URLField(
        _('Company Website Link'),
        max_length=255, unique=True,
        null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{'Company Name:',self.name}"


class DevicesInfo(AbstractBaseModel):
    company = models.ForeignKey(
        CompanyInfo, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    name = models.CharField(
        _('Name'),
        max_length=255, 
        null=True, blank=True
    )
    device_id = models.CharField(
        _('Device Id'),
        max_length=255, unique=True
    )
    checked_out = models.BooleanField(
        default=False
    )
    description = models.TextField(
        blank=True, null=True
    )
    def __str__(self) -> str:
        return f"{'Device Name:',self.name}"
