from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DiscountsConfig(AppConfig):
    name = "shakeomat_api.discounts"
    verbose_name = _("Discounts")

    def ready(self):
        import shakeomat_api.discounts.signals  # noqa F401
