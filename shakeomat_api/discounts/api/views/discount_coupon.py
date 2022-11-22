from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ..serializers import DiscountCouponSerializer
from ...models import DiscountCoupon


class DiscountCouponViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            GenericViewSet):
    serializer_class = DiscountCouponSerializer
    queryset = DiscountCoupon.objects.all()
