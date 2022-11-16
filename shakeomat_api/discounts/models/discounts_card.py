from django.db import models
import uuid

from shakeomat_api.discounts.models._abstract import BaseModel


class DiscountCard(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    card_number = models.IntegerField(
        unique=True,
        verbose_name="Numer Karty"
    )
    phone_number = models.IntegerField(
        verbose_name="Numer telefonu"
    )
    is_active = models.BooleanField(
        verbose_name="Czy Aktywny",
        default=True
    )

    class Meta:
        verbose_name = "Karta Klienta"
