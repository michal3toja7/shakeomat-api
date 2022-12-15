from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from ..serializers import DiscountCouponSerializer
from ...models import DiscountCoupon


class AbstractDiscountCouponViewSet(GenericViewSet):
    serializer_class = DiscountCouponSerializer
    queryset = DiscountCoupon.objects.get_public()

    @action(detail=True, methods=['post'])
    def make_reservation(self, request, pk=None):
        instance: DiscountCoupon = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.make_reservation(instance))

    @action(detail=True, methods=['post'])
    def use_up(self, request, pk=None):
        instance: DiscountCoupon = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.use(instance))

    @action(detail=True, methods=['post'])
    def set_public(self, request, pk=None):
        instance: DiscountCoupon = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.set_public(instance))


class DiscountCouponPublicViewSet(RetrieveModelMixin,
                                  ListModelMixin,
                                  AbstractDiscountCouponViewSet):
    pass


class DiscountCouponViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            AbstractDiscountCouponViewSet):

    def get_queryset(self):
        return DiscountCoupon.objects.get_limited_for_group(self.request.user)

class DiscountCouponReservedViewSet(RetrieveModelMixin,
                            ListModelMixin,
                            AbstractDiscountCouponViewSet):

    def get_queryset(self):
        return DiscountCoupon.objects.get_reserved_by_user(self.request.user)

    @action(detail=True, methods=['post'])
    def undo_reservation(self, request, pk=None):
        instance: DiscountCoupon = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.undo_reservation(instance))

class DiscountCouponCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = DiscountCouponSerializer
    queryset = DiscountCoupon.objects.get_active()
    permission_classes = [HasAPIKey]
