from django.contrib.auth.models import User
from django.db import models
import uuid

from shakeomat_api.discounts.models._abstract import BaseModel
from shakeomat_api.discounts.models._helpers import DISCOUNTS_STATUS, OPTIONAL
from shakeomat_api.discounts.models.discount_coupon import DiscountCoupon
from django.utils.translation import gettext_lazy as _



class DiscountStatus(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    discount_coupon = models.OneToOneField(
        DiscountCoupon,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=DISCOUNTS_STATUS,
        verbose_name=_("Status")
    )
    reserved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **OPTIONAL,
        verbose_name=_("Zarezerwowany przez")
    )
    used_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **OPTIONAL,
        verbose_name=_("Zużyty przez")
    )

    class Meta:
        verbose_name = _("Status zniżki")
        verbose_name_plural = _("Status zniżki")
