from datetime import datetime

from django.db import models
import uuid

from shakeomat_api.discounts.models._abstract import BaseModel
from shakeomat_api.discounts.models._helpers import OPTIONAL, get_end_of_today
from shakeomat_api.discounts.models._helpers import discount_image_path
from shakeomat_api.discounts.models.discount_card import DiscountCard
from django.utils.translation import gettext_lazy as _


class DiscountCoupon(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    discount_card = models.ForeignKey(
        DiscountCard,
        on_delete=models.CASCADE
    )
    discount_image = models.FileField(
        **OPTIONAL, upload_to=discount_image_path,
        verbose_name=_("discound_image")
    )
    discount_title = models.CharField(
        **OPTIONAL,
        max_length=150,
        verbose_name=_("Tytuł")
    )
    discount_description = models.TextField(
        **OPTIONAL,
        verbose_name=_("Opis")
    )
    start_validity_period = models.DateTimeField(
        default=datetime.now,
        verbose_name=_("Początek obowiązywania")
    )
    end_validity_period = models.DateTimeField(
        default=get_end_of_today,
        verbose_name=_("Koniec obowiązywania")
    )

    class Meta:
        verbose_name = _("Kupon Zniżkowy")
        verbose_name_plural = _("Kupony Zniżkowe")
