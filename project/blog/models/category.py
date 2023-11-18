from django.db import models
from autoslug import AutoSlugField

class category_model(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta():
        db_table = "category"
        verbose_name_plural = "categories"
        verbose_name = "category"

    def __str__(self):
        return self.name