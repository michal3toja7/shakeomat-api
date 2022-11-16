from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ..serializers import DiscountCouponSerializer
from ...models import DiscountCoupon


class DiscountCouponViewSet(RetrieveModelMixin, ListModelMixin,
                          UpdateModelMixin,
                          GenericViewSet):
    serializer_class = DiscountCouponSerializer
    queryset = DiscountCoupon
