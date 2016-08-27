from rest_framework import serializers

from ..models import Item


class CreateItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    A ItemSerializer that allows the setting of `slug`.
    """

    class Meta:
        model = Item
        fields = ['slug', 'name', 'serial_number']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Item
        fields = ['slug', 'name', 'serial_number']
