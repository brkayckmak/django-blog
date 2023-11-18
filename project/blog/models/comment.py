from django.db import models
from blog.models import writings_model

class comment_model(models.Model):
    writer = models.ForeignKey("account.custom_user_model", on_delete=models.CASCADE, related_name="comment")
    writing = models.ForeignKey(writings_model, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "comment"
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.writer.username