# Generated by Django 3.0.6 on 2020-05-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorplanscommercialpremises',
            name='alt_attr',
            field=models.CharField(max_length=300, verbose_name='Описание, alt'),
        ),
        migrations.AlterField(
            model_name='imagescommercialpremises',
            name='alt_attr',
            field=models.CharField(max_length=300, verbose_name='Описание, alt'),
        ),
        migrations.AlterField(
            model_name='imagesresidentialcomplex',
            name='alt_attr',
            field=models.CharField(max_length=300, verbose_name='Описание, alt'),
        ),
    ]