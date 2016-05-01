from rest_framework import serializers

from .models import Tenant


class CreateTenantSerializer(serializers.ModelSerializer):
    """
    A TenantSerializer that allows the setting of `slug`.
    """

    class Meta:
        model = Tenant
        fields = ['slug', 'name']


class TenantSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Tenant
        fields = ['slug', 'name']
