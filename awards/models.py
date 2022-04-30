from django.db import models


type_choices = [
    ("Certificado", "Certificado"),
    ("Reconocimiento", "Reconocimiento"),
]

class Awards(models.Model):
    type = models.CharField(max_length=14, choices=type_choices, blank=True, null=True, verbose_name="Certificado/reconocimiento")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    institution = models.CharField(max_length=255, verbose_name="Institución")
    observation = models.CharField(max_length=255, blank=True, null=True, verbose_name="observación")
    date = models.DateField(verbose_name="Fecha", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Certificado - reconocimiento"

    def __str__(self):
        return self.name