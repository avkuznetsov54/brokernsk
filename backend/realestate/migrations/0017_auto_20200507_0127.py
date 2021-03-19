# Generated by Django 3.0.6 on 2020-05-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0016_auto_20200507_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialpremises',
            name='business_category',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_businesscategory', to='realestate.BusinessCategory', verbose_name='Категория бизнеса'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compremises_city', to='realestate.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='communication_systems',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_comsystems', to='realestate.CommunicationSystems', verbose_name='Системы коммуникаций'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='cooker_hood',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compremises_cookerhood', to='realestate.CookerHood', verbose_name='Вытяжка'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='district',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compremises_district', to='realestate.District', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='floor',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_floor', to='realestate.FloorInBuilding', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='purpose_commercial_premise',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_purpose', to='realestate.PurposeOfCommercialPremise', verbose_name='Назначение коммерческого помещения'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compremises_region', to='realestate.Region', verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='relative_location',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_relativelocation', to='realestate.RelativeLocation', verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='residential_complex',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compremises_rescomplex', to='realestate.ResidentialComplex', verbose_name='Жилой комплекс'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='type_entrance',
            field=models.ManyToManyField(blank=True, default=None, related_name='compremises_typeentrance', to='realestate.TypeEntranceToCommercialPremises', verbose_name='Тип входа'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='apart_decoration',
            field=models.ManyToManyField(blank=True, default=None, related_name='rescomplex_apartdecoration', to='realestate.ApartmentDecoration', verbose_name='Отделка'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_city', to='realestate.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='class_of_housing',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_classofhousing', to='realestate.ClassOfHousing', verbose_name='Класс Новостройки'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='deadline',
            field=models.ManyToManyField(blank=True, default=None, related_name='rescomplex_deadline', to='realestate.Deadline', verbose_name='Срок сдачи'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='developer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_developer', to='realestate.Developer', verbose_name='Застройщик'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='district',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_district', to='realestate.District', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='infrastructure',
            field=models.ManyToManyField(blank=True, default=None, related_name='rescomplex_infrastructure', to='realestate.Infrastructure', verbose_name='Инфраструктура'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='material_walls',
            field=models.ManyToManyField(blank=True, default=None, related_name='rescomplex_materialwalls', to='realestate.MaterialWallsOfHouse', verbose_name='Материал стен дома'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='metro_stations',
            field=models.ManyToManyField(blank=True, default=None, related_name='rescomplex_metrostations', to='realestate.NamesOfMetroStations', verbose_name='Название ближайщего метро'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_region', to='realestate.Region', verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='residentialpremise',
            name='floor',
            field=models.ManyToManyField(blank=True, default=None, related_name='respremises_floor', to='realestate.FloorInBuilding', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='residentialpremise',
            name='number_rooms',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respremises_numberrooms', to='realestate.NumberOfRooms', verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='residentialpremise',
            name='res_complex',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='respremises_rescomplex', to='realestate.ResidentialComplex', verbose_name='Жилой комплекс'),
        ),
    ]