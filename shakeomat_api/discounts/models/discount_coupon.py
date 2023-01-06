import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shakeomat_api.discounts.models._abstract import BaseModel
from shakeomat_api.discounts.models._helpers import (
    OPTIONAL,
    RESERVED,
    coupon_image_path,
    get_end_of_today,
)
from shakeomat_api.discounts.models.discount_card import DiscountCard


class DiscountCouponManager(models.Manager):
    def get_active(self):
        qs = self.get_queryset()
        return qs.filter(
            start_validity_period__lte=timezone.now(),
            end_validity_period__gte=timezone.now(),
        )

    def get_public(self):
        return self.get_active().filter(is_public=True)

    def get_limited_for_group(self, user):
        qs = self.get_active()
        return qs.filter(
            is_public=False,
            discount_card__card_group__in=user.card_group.all(),
        )

    def get_reserved_by_user(self, user):
        qs = self.get_active()
        return qs.filter(status__status=RESERVED, status__reserved_by=user)


class DiscountCoupon(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_card = models.ForeignKey(DiscountCard, on_delete=models.CASCADE)
    discount_image = models.FileField(
        upload_to=coupon_image_path, verbose_name=_("discount_image")
    )
    discount_title = models.CharField(
        **OPTIONAL, max_length=150, verbose_name=_("Tytuł")
    )
    discount_description = models.TextField(**OPTIONAL, verbose_name=_("Opis"))
    start_validity_period = models.DateTimeField(
        default=timezone.now, verbose_name=_("Początek obowiązywania")
    )
    end_validity_period = models.DateTimeField(
        default=get_end_of_today, verbose_name=_("Koniec obowiązywania")
    )
    is_public = models.BooleanField(default=False)

    def set_public(self):
        self.is_public = True
        self.save()

    objects = DiscountCouponManager()

    class Meta:
        verbose_name = _("Kupon Zniżkowy")
        verbose_name_plural = _("Kupony Zniżkowe")
