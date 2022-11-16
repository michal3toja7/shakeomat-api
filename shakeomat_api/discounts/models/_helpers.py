OPTIONAL = dict(blank=True, null=True)


def discount_image_path(instance, filename):
    return (
        f"{instance.discount_card.id}"
        f"/{instance.id}"
    )
