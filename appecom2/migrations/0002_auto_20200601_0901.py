# Generated by Django 3.0.3 on 2020-06-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appecom2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]