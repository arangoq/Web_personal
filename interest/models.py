from django.db import models
from ckeditor.fields import RichTextField


class Interest(models.Model):
    interest = RichTextField(null=True, blank=True, max_length=512, verbose_name="Habilidades")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Interés"
        ordering = ["-created"]