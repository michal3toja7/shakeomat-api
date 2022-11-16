from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ..serializers import DiscountCardSerializer
from ...models import DiscountCard


class DiscountCardViewSet(RetrieveModelMixin, ListModelMixin,
                          UpdateModelMixin,
                          GenericViewSet):
    serializer_class = DiscountCardSerializer
    queryset = DiscountCard
