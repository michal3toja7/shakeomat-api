import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from shakeomat_api.discounts.models._abstract import BaseModel

User = get_user_model()

class DiscountCard(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Właściciel"),
        related_name="card_owner"
    )
    card_number = models.BigIntegerField(
        unique=True, verbose_name=_("Numer Karty")
    )
    phone_number = models.BigIntegerField(
        unique=True, verbose_name=_("Numer telefonu")
    )
    is_active = models.BooleanField(
        verbose_name=_("Czy Aktywny"), default=True
    )

    class Meta:
        verbose_name = _("Karta Klienta")
        verbose_name_plural = _("Karty Klientów")
