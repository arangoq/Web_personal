from django.db import models
from ckeditor.fields import RichTextField

present_choices = [
    ("A", "Actualmente"),
]

class Experience(models.Model):
    position = models.CharField(max_length=255, verbose_name="Cargo/puesto")
    company = models.CharField(max_length=255, verbose_name="Empresa/Institución")
    Functions = RichTextField(null=True, blank=True, max_length=512, verbose_name="Funciones")
    start_date = models.DateField(verbose_name="Fecha ingreso")
    final_date = models.DateField(verbose_name="Fecha salida", blank=True, null=True)
    present = models.CharField(max_length=1, choices=present_choices, blank=True, null=True, verbose_name="Actualmente")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Experiencia"
        ordering = ["-created"]

    def __str__(self):
        return self.position




