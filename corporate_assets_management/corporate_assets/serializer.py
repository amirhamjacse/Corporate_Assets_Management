from rest_framework import serializers
from .models import (
    EmployeeInfo, CompanyInfo, DevicesInfo
)


class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class DevicesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesInfo
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(
        source='companyinfo.name'
    )
    device_info = DevicesInfoSerializer(
        many=True, read_only=True,
    )

    class Meta:
        model = EmployeeInfo
        fields = [
            'id',
            'user',
            'company_name',
            'device_info'
        ]
