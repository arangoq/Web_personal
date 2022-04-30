from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


class About(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    lastname = models.CharField(max_length=255, verbose_name="Apellido")
    degree = models.CharField(max_length=255, verbose_name="Título")
    postgraduate = models.CharField(max_length=255, verbose_name="Posgrado")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    mail = models.EmailField(verbose_name="Correo electrónico")
    phone = models.CharField(max_length=10, verbose_name="Teléfono")
    profile = RichTextField(null=True, blank=True, max_length=512, verbose_name="Perfil")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Acerca de"

    def clean(self):
        response=""
        if len(self.phone) != 7 and len(self.phone) != 10:
            response += "Error!! Por favor verificar el número teléfonico, la logitud debe ser 7 números (fijo) o 10 números (cel)"
        if not self.phone.isdigit():
            response +="Error!! Por favor verificar el número teléfonico, solo se deben ingresar valores numéricos"

        if response:
            raise ValidationError(response)

    def __str__(self):
        return self.name




