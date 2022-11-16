class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dodano")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Zaktualizowano"
    )

    class Meta:
        abstract = True
