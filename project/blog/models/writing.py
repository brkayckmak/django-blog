from django.db import models
from autoslug import AutoSlugField
from blog.models import category_model
from ckeditor.fields import RichTextField
from blog.abstract_model import data_abstract_model

class writings_model(data_abstract_model):
    image = models.ImageField(upload_to="writing_images")
    title = models.CharField(max_length=50, blank=False, null=False)
    content = RichTextField()
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(category_model, related_name="writing")
    writer = models.ForeignKey("account.custom_user_model", related_name="writings", on_delete=models.CASCADE)

    class Meta():
        db_table = "writing"
        verbose_name = "writing"
        verbose_name_plural = "writings"

    def __str__(self):
        return self.title
