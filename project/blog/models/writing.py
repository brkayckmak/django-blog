from django.db import models
from autoslug import AutoSlugField
from blog.models import category_model
from django.contrib.auth.models import User

class writings_model(models.Model):
    image = models.ImageField(upload_to="writing_images")
    title = models.CharField(max_length=50, blank=False, null=False)
    writing = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from=title, unique=True)
    categories = models.ManyToManyField(category_model, related_name="writing")
    writer = models.ForeignKey(User, related_name="writings", on_delete=models.CASCADE)

    class Meta():
        db_table = "writings"
        verbose_name = "writing"
        verbose_name_plural = "writings"