from django.db import models
from ckeditor.fields import RichTextField

status_choices = [
    ("C", "Cursando"),
    ("G", "Graduado"),
]

class Education(models.Model):
    university = models.CharField(max_length=255, verbose_name="Universidad")
    degree = models.CharField(max_length=255, verbose_name="Título")
    note = RichTextField(null=True, blank=True, max_length=512, verbose_name="Nota/Observación")
    start_date = models.DateField(verbose_name="Fecha inicio")
    final_date = models.DateField(verbose_name="Fecha finalización", blank=True, null=True)
    status = models.CharField(max_length=1, choices=status_choices, blank=True, null=True, verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Educación"
        ordering = ["-created"]

    def __str__(self):
        return self.degree