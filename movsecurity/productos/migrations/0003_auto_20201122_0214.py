# Generated by Django 3.0.5 on 2020-11-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20201121_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(max_length=45),
        ),
    ]