from rest_framework import serializers

from shakeomat_api.discounts.models import DiscountStatus
from shakeomat_api.users.api.serializers import UserSerializer


class DiscountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountStatus
        fields = "__all__"


class DiscountStatusShortSerializer(DiscountStatusSerializer):
    reserved_by = UserSerializer(many=False)
    used_by = UserSerializer(many=False)

    class Meta:
        model = DiscountStatus
        fields = [
            "status",
            "reserved_by",
            "used_by"
        ]
