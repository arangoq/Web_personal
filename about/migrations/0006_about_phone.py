# Generated by Django 4.0.3 on 2022-04-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_rename_create_about_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(default=1, max_length=10, verbose_name='Teléfono'),
            preserve_default=False,
        ),
    ]