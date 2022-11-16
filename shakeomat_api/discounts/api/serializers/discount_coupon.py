from rest_framework import serializers

from shakeomat_api.discounts.models import DiscountCoupon


class DiscountCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = ["__all__"]
