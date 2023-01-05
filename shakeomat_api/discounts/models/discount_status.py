import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from shakeomat_api.discounts.models._abstract import BaseModel
from shakeomat_api.discounts.models._helpers import (
    DISCOUNTS_STATUS,
    NEW,
    OPTIONAL,
    RESERVED,
    USED,
)
from shakeomat_api.discounts.models.discount_coupon import DiscountCoupon

User = get_user_model()


class DiscountStatus(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount_coupon = models.OneToOneField(
        DiscountCoupon, on_delete=models.CASCADE, related_name="status"
    )
    status = models.CharField(
        choices=DISCOUNTS_STATUS,
        verbose_name=_("Status"),
        max_length=20,
        default=NEW,
    )
    reserved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **OPTIONAL,
        verbose_name=_("Zarezerwowany przez"),
        related_name="reserved_by"
    )
    used_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **OPTIONAL,
        verbose_name=_("Zużyty przez"),
        related_name="used_by"
    )

    def reserve(self, user: User) -> bool:
        if self.status in {RESERVED, USED}:
            return False
        self.status = RESERVED
        self.reserved_by = user
        self.save()
        return True

    def undo_reserve(self) -> bool:
        if self.status in {NEW}:
            return False
        self.status = NEW
        self.reserved_by = None
        self.save()
        return True

    def use(self, user: User) -> bool:
        if self.status == USED:
            return False
        self.status = USED
        self.used_by = user
        self.save()
        return True

    class Meta:
        verbose_name = _("Status zniżki")
        verbose_name_plural = _("Statusy zniżek")
