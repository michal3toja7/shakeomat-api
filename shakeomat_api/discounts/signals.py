from django.db.models.signals import post_save
from django.dispatch import receiver

from shakeomat_api.discounts.models import DiscountCoupon
from shakeomat_api.discounts.models import DiscountStatus


@receiver(post_save, sender=DiscountCoupon)
def create_status(sender, instance: DiscountCoupon, created, **kwargs):
    """
    Django Signals. The function is called when a DiscountCoupon object is
    created. It creates a statis object related to the one-to-one
    relationship with the DiscountCoupon.
    """
    print("Co do chuja?")
    if created:
        DiscountStatus.objects.create(discount_coupon=instance)
