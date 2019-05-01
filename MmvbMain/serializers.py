from rest_framework import serializers

from .models import Regions


class RegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regions
        fields = (
            'url',
            'administrative_name',
            'comment',
            'munitipal_name',
            'okato_code',
            'oktmo_code',
            'postcode',
            'state_uuid',
        )
