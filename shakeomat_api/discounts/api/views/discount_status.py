from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ...models import DiscountStatus
from ..serializers import DiscountStatusSerializer


class DiscountStatusViewSet(
    RetrieveModelMixin, ListModelMixin, GenericViewSet
):
    serializer_class = DiscountStatusSerializer
    queryset = DiscountStatus.objects.all()
