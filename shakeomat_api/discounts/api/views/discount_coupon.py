from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
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
