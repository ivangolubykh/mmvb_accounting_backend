from rest_framework import serializers

from .models import BrokerageAccounts
from .models import Issuers
from .models import Regions


class BrokerageAccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrokerageAccounts
        fields = (
            'url',
            'comment',
            'name',
        )


class IssuersSerializer(serializers.HyperlinkedModelSerializer):
    region_name = serializers.SerializerMethodField()

    def get_region_name(self, obj):
        if obj.regions:
            return obj.regions.munitipal_name

    class Meta:
        model = Issuers
        fields = (
            'url',
            'comment',
            'name',
            'ogrn',
            'regions',
            'region_name',
            'site',
        )


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


class RegionsNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = (
            # 'id',
            'url',
            'munitipal_name',
        )
