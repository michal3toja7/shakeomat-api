from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ..serializers import DiscountStatusSerializer
from ...models import DiscountStatus


class DiscountStatusViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            GenericViewSet):
    serializer_class = DiscountStatusSerializer
    queryset = DiscountStatus.objects.all()
