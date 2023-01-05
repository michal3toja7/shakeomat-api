from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from shakeomat_api.discounts.api.views import (
    DiscountCardViewSet,
    DiscountCouponCreateViewSet,
    DiscountCouponPublicViewSet,
    DiscountCouponReservedViewSet,
    DiscountCouponViewSet,
    DiscountStatusViewSet,
)
from shakeomat_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("discount-coupon", DiscountCouponViewSet)
router.register("discount-reserved-coupon", DiscountCouponReservedViewSet)
router.register("create-discount-coupon", DiscountCouponCreateViewSet)
router.register("discount-public-coupon", DiscountCouponPublicViewSet)
router.register("discount-status", DiscountStatusViewSet)
router.register("client-card", DiscountCardViewSet)


app_name = "api"
urlpatterns = router.urls
