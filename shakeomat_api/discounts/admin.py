from django.contrib import admin

from shakeomat_api.discounts.models import (
    DiscountCard,
    DiscountCoupon,
    DiscountStatus,
)
from shakeomat_api.discounts.models.discount_card_group import (
    DiscountCardGroup,
)


class DiscountStatusInlineAdmin(admin.StackedInline):
    model = DiscountStatus


@admin.register(DiscountCoupon)
class DiscountCouponAdmin(admin.ModelAdmin):
    inlines = (DiscountStatusInlineAdmin,)

    pass


@admin.register(DiscountCardGroup)
class DiscountCardGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscountCard)
class DiscountCardAdmin(admin.ModelAdmin):
    pass
