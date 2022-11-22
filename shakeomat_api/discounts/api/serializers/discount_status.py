from rest_framework import serializers

from shakeomat_api.discounts.models import DiscountStatus


class DiscountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountStatus
        fields = "__all__"
