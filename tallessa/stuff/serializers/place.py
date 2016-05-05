from rest_framework import serializers

from ..models import Place


class CreatePlaceSerializer(serializers.HyperlinkedModelSerializer):
    """
    A PlaceSerializer that allows the setting of `slug`.
    """

    class Meta:
        model = Place
        fields = ['slug', 'name']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Place
        fields = ['slug', 'name']
