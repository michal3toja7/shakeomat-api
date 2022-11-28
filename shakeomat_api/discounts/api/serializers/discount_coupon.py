from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from rest_framework.decorators import action

from shakeomat_api.discounts.api.serializers.discount_card import \
    DiscountCardSerializer
from shakeomat_api.discounts.api.serializers.discount_status import \
    DiscountStatusShortSerializer
from shakeomat_api.discounts.models import DiscountCoupon, DiscountCard


class DiscountCouponSerializer(serializers.ModelSerializer):
    discount_card = DiscountCardSerializer(many=False, read_only=True)
    discount_status = DiscountStatusShortSerializer(many=False,
                                                    read_only=True)
    phone_number = serializers.IntegerField(
        write_only=True,
        required=False,
        help_text=_("A field that searches for the customer's card by"
                    " phone number")
    )
    card_number = serializers.IntegerField(
        write_only=True, required=False,
        help_text="A field that searches for a customer's card by card number")

    class Meta:
        model = DiscountCoupon
        fields = [
            "phone_number",
            "card_number",
            "discount_status",
            "discount_image",
            "discount_title",
            "discount_description",
            "start_validity_period",
            "end_validity_period",
            "discount_card",
        ]

    def create(self, validated_data):
        if validated_data.get("phone_number"):
            validated_data["discount_card"] = DiscountCard.objects.get(
                phone_number=validated_data.pop("phone_number")
            )
        elif validated_data.get("card_number"):
            validated_data["discount_card"] = DiscountCard.objects.get(
                card_number=validated_data.pop("card_number")
            )
        else:
            #ToDo Finish this
            raise

        return super().create(validated_data)
