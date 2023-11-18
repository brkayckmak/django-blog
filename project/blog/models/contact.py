from django.db import models

class contact_model(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = "contact"
        verbose_name = "contact"
        verbose_name_plural = "contact"

    def __str__(self):
        return self.email
        
