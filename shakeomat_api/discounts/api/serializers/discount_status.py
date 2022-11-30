from rest_framework import serializers

from shakeomat_api.discounts.models import DiscountStatus
from shakeomat_api.users.api.serializers import UserShortSerializer


class DiscountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountStatus
        fields = "__all__"


class DiscountStatusShortSerializer(DiscountStatusSerializer):
    reserved_by = serializers.CharField(read_only=True)
    used_by = serializers.CharField(read_only=True)

    class Meta:
        model = DiscountStatus
        fields = [
            "status",
            "reserved_by",
            "used_by"
        ]
