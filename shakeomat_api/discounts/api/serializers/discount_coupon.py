from rest_framework import serializers

from shakeomat_api.discounts.api.serializers.discount_card import \
    DiscountCardSerializer
from shakeomat_api.discounts.api.serializers.discount_status import \
    DiscountStatusShortSerializer
from shakeomat_api.discounts.models import DiscountCoupon


class DiscountCouponSerializer(serializers.ModelSerializer):
    discount_status = DiscountStatusShortSerializer(many=False, read_only=True)
    discount_card = DiscountCardSerializer(many=False, read_only=True)

    class Meta:
        model = DiscountCoupon
        fields = [
            "discount_status",
            "discount_image",
            "discount_title",
            "discount_description",
            "start_validity_period",
            "end_validity_period",
            "discount_card",
        ]
        # fields += "discount_status"
