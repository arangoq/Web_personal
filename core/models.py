from django.db import models

class Core(models.Model):
    image = models.ImageField(verbose_name="Imagen de perfil", upload_to="Core")

    class Meta:
        verbose_name = "Imagen de perfil"

