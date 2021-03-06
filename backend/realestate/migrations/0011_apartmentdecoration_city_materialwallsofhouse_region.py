# Generated by Django 3.0.6 on 2020-05-06 14:00

from django.db import migrations, models
import realestate.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0010_auto_20200506_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentDecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Отделка квартиры',
                'verbose_name_plural': 'Отделки квартиры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Материал дома')),
                ('main_image', models.FileField(blank=True, null=True, upload_to=realestate.models.generate_url_for_image, verbose_name='Главное изображение Города')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MaterialWallsOfHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Материал стен дома')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Материал стен дома',
                'verbose_name_plural': 'Материалы стен дома',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Материал дома')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
                'ordering': ['name'],
            },
        ),
    ]
