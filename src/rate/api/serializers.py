from rate.models import Rate

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id', 'amount',
            'created', 'get_source_display',
            'source', 'currency_type', 'type',
            'get_currency_type_display', 'get_type_display'
        )
