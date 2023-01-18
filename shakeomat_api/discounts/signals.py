from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


from shakeomat_api.discounts.models import DiscountCoupon
from shakeomat_api.discounts.models import DiscountStatus
from shakeomat_api.discounts.models import DiscountCard
from shakeomat_api.discounts.models import DiscountCardGroup
from shakeomat_api.image_processing import ImageProcessing


@receiver(post_save, sender=DiscountCoupon)
def create_status(sender, instance: DiscountCoupon, created, **kwargs):
    """
    Django Signals. The function is called when a DiscountCoupon object is
    created. It creates a statis object related to the one-to-one
    relationship with the DiscountCoupon.
    """
    if created:
        DiscountStatus.objects.create(discount_coupon=instance)
        image = ImageProcessing(instance.discount_image)
        image.image_process()
        image.save()


@receiver(post_save, sender=DiscountCard)
def create_group(sender, instance: DiscountCard, created, **kwargs):
    """
    Django Signals. The function is called when a DiscountCard object is
    created. It creates a object group with user owner.
    """
    if created:
        discount_group, is_new = DiscountCardGroup.objects.get_or_create(
            owner=instance.owner,
            defaults={"name": f'{_("Domyślna grupa")} - {instance.owner}'})
        discount_group.discount_cards.add(instance)
        discount_group.save()
