# Generated by Django 4.2.8 on 2023-12-19 13:25

import Revisorer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revisorer', '0002_alter_revisor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisor',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=Revisorer.models.get_rapport_path),
        ),
    ]
