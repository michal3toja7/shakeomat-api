from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


from ..serializers import DiscountStatusSerializer
from ...models import DiscountStatus


class DiscountStatusViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            GenericViewSet):
    serializer_class = DiscountStatusSerializer
    queryset = DiscountStatus.objects.all()
