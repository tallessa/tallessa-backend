from rest_framework import serializers

from ..models import Team


class CreateTeamSerializer(serializers.HyperlinkedModelSerializer):
    """
    A TeamSerializer that allows the setting of `slug`.
    """

    class Meta:
        model = Team
        fields = ['slug', 'name']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Team
        fields = ['slug', 'name']
