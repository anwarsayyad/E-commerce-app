"""Serilaizer for the store realted API's"""

from rest_framework import serializers

from core.models import (
    Items
)

class ItemsSerializer(serializers.ModelSerializer):
    """Serializer class for the Items"""

    class Meta:
        model = Items
        fields = ['id',
                  'title',
                  'price',
                  'discount_price',
                  'category',
                  'label',
                 ]
        read_only_fields = ['id']
        
