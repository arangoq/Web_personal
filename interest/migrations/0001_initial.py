# Generated by Django 4.0.3 on 2022-04-29 03:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', ckeditor.fields.RichTextField(blank=True, max_length=512, null=True, verbose_name='Habilidades')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Interés',
                'ordering': ['-created'],
            },
        ),
    ]
