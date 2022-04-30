from django.db import models
from ckeditor.fields import RichTextField


class Skills(models.Model):
    skills = RichTextField(null=True, blank=True, max_length=512, verbose_name="Habilidades")
    core_skills = RichTextField(null=True, blank=True, max_length=512, verbose_name="Aptitudes principales")
    computer_tools = RichTextField(null=True, blank=True, max_length=512, verbose_name="Herramientas informaticas")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Habilidades"
        ordering = ["-created"]
