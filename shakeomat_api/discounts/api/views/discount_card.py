from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ...models import DiscountCard
from ..serializers import DiscountCardSerializer


class DiscountCardViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = DiscountCardSerializer
    queryset = DiscountCard.objects.all()
