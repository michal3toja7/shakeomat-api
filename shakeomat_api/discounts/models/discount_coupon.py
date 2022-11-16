from django.db import models
import uuid

from shakeomat_api.discounts.models._abstract import BaseModel
from shakeomat_api.discounts.models._helpers import OPTIONAL
from shakeomat_api.discounts.models._helpers import discount_image_path
from shakeomat_api.discounts.models.discounts_card import DiscountCard


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
        verbose_name="discound_image"
    )
    discount_title = models.CharField(
        **OPTIONAL,
        max_length=150,
        verbose_name="Tytuł"
    )
    discount_description = models.TextField(
        **OPTIONAL,
        verbose_name="Opis"
    )

    class Meta:
        verbose_name = "Kupon Zniżkowy"
