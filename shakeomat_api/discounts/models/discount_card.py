import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from shakeomat_api.discounts.models._abstract import BaseModel


class DiscountCard(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_number = models.IntegerField(
        unique=True, verbose_name=_("Numer Karty")
    )
    phone_number = models.IntegerField(
        unique=True, verbose_name=_("Numer telefonu")
    )
    is_active = models.BooleanField(
        verbose_name=_("Czy Aktywny"), default=True
    )

    class Meta:
        verbose_name = _("Karta Klienta")
        verbose_name_plural = _("Karty Klientów")
