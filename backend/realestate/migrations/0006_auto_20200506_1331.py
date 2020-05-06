# Generated by Django 3.0.6 on 2020-05-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_auto_20200506_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nameofnearestmetro',
            options={'ordering': ['name'], 'verbose_name': 'Название ближайщего(-их) метро', 'verbose_name_plural': 'Названии ближайщего(-их) метро'},
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='ready_commercial_premise',
            field=models.CharField(blank=True, choices=[('building', 'Строящее'), ('finished', 'Готовое')], db_index=True, max_length=25, verbose_name='Готовность помещения'),
        ),
    ]