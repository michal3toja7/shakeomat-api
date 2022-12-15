from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from shakeomat_api.discounts.api.serializers.discount_card import \
    DiscountCardSerializer
from shakeomat_api.discounts.api.serializers.discount_status import \
    DiscountStatusShortSerializer
from shakeomat_api.discounts.models import DiscountCoupon, DiscountCard


class DiscountCouponSerializer(serializers.ModelSerializer):
    discount_card = DiscountCardSerializer(many=False, read_only=True)
    status = DiscountStatusShortSerializer(many=False, read_only=True)
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
            "id",
            "status",
            "phone_number",
            "card_number",
            "discount_image",
            "discount_title",
            "discount_description",
            "start_validity_period",
            "end_validity_period",
            "discount_card",
            "is_public",
        ]

    def create(self, validated_data):
        try:
            if validated_data.get("phone_number"):
                validated_data.pop("card_number", None)
                validated_data["discount_card"] = DiscountCard.objects.get(
                    phone_number=validated_data.pop("phone_number")
                )
            elif validated_data.get("card_number"):
                validated_data["discount_card"] = DiscountCard.objects.get(
                    card_number=validated_data.pop("card_number")
                )
            else:
                raise serializers.ValidationError(
                    "Customer card details have not been provided")
        except DiscountCard.DoesNotExist:
            raise serializers.ValidationError(
                "Incorrect phone number or customer card number"
            )

        return super().create(validated_data)

    def make_reservation(self, discount_coupon: DiscountCoupon):
        try:
            if discount_coupon.status.reserve(self.context["request"].user):
                return self.data
        except AttributeError:
            pass
        raise serializers.ValidationError("The coupon is already reserved")
    def undo_reservation(self, discount_coupon: DiscountCoupon):
        try:
            if discount_coupon.status.undo_reserve():
                return self.data
        except AttributeError:
            pass
        raise serializers.ValidationError("The coupon is already reserved")

    def use(self, discount_coupon: DiscountCoupon):
        try:
            if discount_coupon.status.use(self.context["request"].user):
                return self.data
        except AttributeError:
            pass
        raise serializers.ValidationError("The coupon is already used")

    def set_public(self, discount_coupon: DiscountCoupon):
        if discount_coupon.is_public:
            return self.data
        discount_coupon.set_public()
        return self.data
