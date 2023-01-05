import os.path
from datetime import datetime

from django.utils.translation import gettext_lazy as _

OPTIONAL = dict(blank=True, null=True)


def coupon_image_path(instance, filename):
    return (
        f"{instance.discount_card.id}"
        f"/{instance.id}{get_extension(filename)}"
    )


def get_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]


def get_end_of_today() -> datetime:
    return datetime.now().replace(hour=23, minute=59)


NEW = "NEW"
RESERVED = "RESERVED"
USED = "USED"
EXPIRED = "EXPIRED"

DISCOUNTS_STATUS = (
    (NEW, _("Nowy")),
    (RESERVED, _("Zarezerwowany")),
    (USED, _("Zużyty")),
    (EXPIRED, _("Przeterminowany")),
)
