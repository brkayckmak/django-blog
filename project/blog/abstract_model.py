from django.db import models

class data_abstract_model(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True