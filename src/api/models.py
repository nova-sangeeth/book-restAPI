from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class book_store(models.Model):
    title = models.CharField(max_length=256, null=True)
    genre = models.CharField(max_length=64, null=True)
    link = models.URLField(null=True, max_length=512)
    author = models.CharField(max_length=128, null=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title
