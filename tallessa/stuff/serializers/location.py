from rest_framework import serializers

from ..models import Location


class CreateLocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    A LocationSerializer that allows the setting of `slug`.
    """

    class Meta:
        model = Location
        fields = ['slug', 'name']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Location
        fields = ['slug', 'name']
