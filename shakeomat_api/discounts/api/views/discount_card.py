from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from ..serializers import DiscountCardSerializer
from ...models import DiscountCard


class DiscountCardViewSet(RetrieveModelMixin,
                          ListModelMixin,
                          CreateModelMixin,
                          UpdateModelMixin,
                          GenericViewSet):
    serializer_class = DiscountCardSerializer
    queryset = DiscountCard.objects.all()
