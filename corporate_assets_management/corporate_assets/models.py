from django.db import models
from django.contrib.auth.models import User
from corporate_assets_management.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


#Store Employee Data with User
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


#Store Company Information
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
    device_image = models.FileField(
        _('Device Image'),
        blank=True, null=True
    )
    website = models.URLField(
        _('Company Website Link'),
        max_length=255, unique=True,
        null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{'Company Name:',self.name}"


#Devices Informations
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
        _('Checkout'),
        default=False
    )
    description = models.TextField(
        _('Descriptions'),
        blank=True, null=True
    )
    def __str__(self) -> str:
        return f"{'Device Name:',self.name}"


#Log of device checkouot with condition
class DeviceCheckoutLog(AbstractBaseModel):
    device = models.ForeignKey(DevicesInfo,
        on_delete=models.CASCADE
    )
    employee = models.ForeignKey(EmployeeInfo,
        on_delete=models.CASCADE
    )
    date_of_checkout = models.DateTimeField(
        _('Checkout Date'),
        null=True, blank=True
    )
    date_of_return = models.DateTimeField(
        _('Return Date'),
        null=True, blank=True
    )
    checked_out = models.BooleanField(
        _('Checkout or not'),
        default=False
    )
    checked_out = models.BooleanField(
        _('Returned'),
        default=False
    )

    def __str__(self):
        return f"{self.checkout_date}"

    