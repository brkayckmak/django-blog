from django.db import models
from autoslug import AutoSlugField
from blog.models import category_model
from ckeditor.fields import RichTextField

class writings_model(models.Model):
    image = models.ImageField(upload_to="writing_images")
    title = models.CharField(max_length=50, blank=False, null=False)
    content = RichTextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    categories = models.ManyToManyField(category_model, related_name="writing")
    writer = models.ForeignKey("account.custom_user_model", related_name="writings", on_delete=models.CASCADE)

    class Meta():
        db_table = "writing"
        verbose_name = "writing"
        verbose_name_plural = "writings"

    def __str__(self):
        return self.title
