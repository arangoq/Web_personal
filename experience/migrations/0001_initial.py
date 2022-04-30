# Generated by Django 4.0.3 on 2022-04-28 21:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='Cargo/puesto')),
                ('company', models.CharField(max_length=255, verbose_name='Empresa/Institución')),
                ('Functions', ckeditor.fields.RichTextField(blank=True, max_length=512, null=True, verbose_name='Funciones')),
                ('start_date', models.DateField(verbose_name='Fecha ingreso')),
                ('final_date', models.DateField(blank=True, null=True, verbose_name='Fecha salida')),
                ('present', models.CharField(blank=True, choices=[('A', 'Actualmente')], max_length=1, null=True, verbose_name='Actualmente')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Experiencia',
            },
        ),
    ]