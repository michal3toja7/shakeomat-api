from django.contrib.auth import get_user_model
from django.db import models

from shakeomat_api.discounts.models.discount_card import DiscountCard
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DiscountCardGroups(models.Model):
    name = models.CharField(
        max_length=200
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Właściciel grupy")
    )
    users = models.ManyToManyField(
        User,
        blank=True,
        verbose_name=_("Członkowie grupy")
    )
    discount_cards = models.ManyToManyField(
        DiscountCard,
        blank=True,
        verbose_name=_("Karty klienta")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Grupa kart zniżkowych"
        verbose_name_plural = "Grupy kart zniżkowych"
