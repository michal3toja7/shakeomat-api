from rest_framework import serializers

from shakeomat_api.discounts.models import DiscountCard


class DiscountCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCard
        fields = ["__all__"]
