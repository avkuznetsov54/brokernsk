from django.db import models
import datetime


# ф-ция генерит путь для загружаемого файла
def generate_url_for_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s' % (now.year, now.month, now.day, filename)
    return url


class District(models.Model):
    """Модель Района"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Район')
    subname = models.CharField(max_length=10, unique=True, blank=True, verbose_name='Сокращённое название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['name']


class DeadlineNewBuilding(models.Model):
    """Модель Срок сдачи Новостройки"""
    full_date = models.CharField(max_length=10, unique=True, verbose_name='Срок сдачи')
    only_year = models.IntegerField(db_index=True, verbose_name='Год срока сдачи')
    only_quarter = models.IntegerField(db_index=True, verbose_name='Квартал срока сдачи')

    def __str__(self):
        return self.full_date

    class Meta:
        verbose_name = 'Срок сдачи'
        verbose_name_plural = 'Сроки сдачи'
        # ordering = ['name']


class Developer(models.Model):
    """Модель Застройщик"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Застройщик')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class ClassNewBuilding(models.Model):
    """Модель Класс Новостройки"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Новостройки'
        verbose_name_plural = 'Классы Новостроек'
        ordering = ['name']


class BusinessCategory(models.Model):
    """Модель Категория бизнеса"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория бизнеса'
        verbose_name_plural = 'Категории бизнесов'
        ordering = ['name']


class PurposeOfCommercialPremise(models.Model):
    """Модель Назначение помещения"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Назначение помещения'
        verbose_name_plural = 'Назначении помещений'
        ordering = ['name']


class CookerHood(models.Model):
    """Модель Вытяжка"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вытяжка'
        verbose_name_plural = 'Вытяжки'
        ordering = ['name']


class TypeEntranceToCommercialPremises(models.Model):
    """Модель Тип входа в коммерческое помещение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип входа в коммерческое помещение'
        verbose_name_plural = 'Типы входов в коммерческое помещение'
        ordering = ['name']


class CommunicationSystems(models.Model):
    """Модель Системы коммуникаций"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Системы коммуникаций'
        verbose_name_plural = 'Системы коммуникаций'
        ordering = ['name']


class FloorInBuilding(models.Model):
    """Модель Этаж в здании"""
    num_floor = models.IntegerField(db_index=True, verbose_name='Этаж')

    def __str__(self):
        return f'{self.num_floor}'

    class Meta:
        verbose_name = 'Этаж в здании'
        verbose_name_plural = 'Этажи в здании'
        ordering = ['num_floor']


class RelativeLocation(models.Model):
    """Модель Расположение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
        ordering = ['name']


class NameOfNearestMetro(models.Model):
    """Модель Название ближайщего метро"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название ближайщего метро'
        verbose_name_plural = 'Названии ближайщего метро'
        ordering = ['name']


class ResidentialComplex(models.Model):
    """Модель Жилого Комплекса"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Название ЖК')
    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Застройщик',
                                  related_name="developer",
                                  default=None,
                                  null=True,
                                  blank=True)
    class_new_building = models.ForeignKey(ClassNewBuilding,
                                           on_delete=models.SET_NULL,
                                           verbose_name='Класс Новостройки',
                                           related_name='classnewbuilding',
                                           default=None,
                                           null=True,
                                           blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='districtresidentialcomplex',
                                 default=None,
                                 null=True,
                                 blank=True)
    address = models.CharField(max_length=150, db_index=True, verbose_name='Адрес',
                               default=None,
                               null=True, blank=True)
    one_or_many_buildings = models.BooleanField(default=False, verbose_name='В ЖК несколько строений')

    number_of_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность')
    min_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность min')
    max_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность max')

    house_completed = models.BooleanField(default=False, verbose_name='Дом сдан, Да/Нет')
    deadline = models.ManyToManyField(DeadlineNewBuilding,
                                      verbose_name='Срок сдачи',
                                      related_name='deadline',
                                      default=None,
                                      blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение ЖК")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    distance_to_metro = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Растояние до метро, м')
    name_of_nearest_metro = models.ManyToManyField(NameOfNearestMetro,
                                                   verbose_name='Название ближайщего метро',
                                                   related_name='nameofnearestmetro',
                                                   default=None,
                                                   blank=True)

    site_developer = models.URLField(max_length=300,
                                     verbose_name='Сайт застройщика/Новостройки',
                                     default=None,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жилой Комплекс'
        verbose_name_plural = 'Жилые Комплексы'
        ordering = ['name']


class CommercialPremises(models.Model):
    """Модель Коммерческого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    is_sale = models.BooleanField(default=False, verbose_name='Продажа')
    is_rent = models.BooleanField(default=False, verbose_name='Аренда')

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    floor = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этаж')
    several_floors = models.BooleanField(default=False, verbose_name='Помещение с несколькими этажами')

    address = models.CharField(max_length=150, db_index=True, default=None, verbose_name='Адрес')
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='districtcommercialpremises',
                                 default=None,
                                 null=True,
                                 blank=True)
    relative_location = models.ManyToManyField(RelativeLocation,
                                               verbose_name='Расположение',
                                               related_name='relativelocation',
                                               default=None,
                                               blank=True)

    residential_complex = models.ForeignKey(ResidentialComplex,
                                            on_delete=models.SET_NULL,
                                            verbose_name='Жилой комплекс',
                                            related_name='residentialcomplex',
                                            default=None,
                                            null=True,
                                            blank=True)

    READY_CHOICES = (
        ('building', 'Строящее'),
        ('finished', 'Готовое')
    )

    ready_commercial_premise = models.CharField(choices=READY_CHOICES, max_length=25, db_index=True, blank=True,
                                                verbose_name='Готовность помещения')

    purpose_commercial_premise = models.ManyToManyField(PurposeOfCommercialPremise,
                                                        verbose_name='Назначение коммерческого помещения',
                                                        related_name='purposecommercialpremise',
                                                        default=None,
                                                        blank=True)
    business_category = models.ManyToManyField(BusinessCategory,
                                               verbose_name='Категория бизнеса',
                                               related_name='businesscategory',
                                               default=None,
                                               blank=True)
    rent_price = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Стоимость аренды, руб/мес.')
    cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Стоймость на продажу')
    min_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость от, мес')
    max_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость до, мес')
    min_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка, от')
    max_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка, до')
    possible_income = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Возможный доход')

    kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт')
    min_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, от')
    max_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, до')

    communication_systems = models.ManyToManyField(CommunicationSystems,
                                                   verbose_name='Системы коммуникаций',
                                                   related_name='communicationsystems',
                                                   default=None,
                                                   blank=True)
    cooker_hood = models.ForeignKey(CookerHood,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Вытяжка',
                                    related_name='cookerhood',
                                    default=None,
                                    null=True,
                                    blank=True)
    type_entrance = models.ManyToManyField(TypeEntranceToCommercialPremises,
                                           verbose_name='Тип входа',
                                           related_name='typeentrance',
                                           default=None,
                                           blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение помещения")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Коммерческое помещение'
        verbose_name_plural = 'Коммерческие помещения'
        # ordering = ['name']


class ImagesResidentialComplex(models.Model):
    """Модель Изображение Жилого Комплекса"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="Описание, alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение")
    residential_complex = models.ForeignKey(ResidentialComplex, verbose_name="Жилой Комплекс", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Изображение Жилого Комплекса"
        verbose_name_plural = "Изображения Жилого Комплекса"


class ImagesCommercialPremises(models.Model):
    """Модель Изображение Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="Описание, alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение")
    commercial_premises = models.ForeignKey(CommercialPremises, verbose_name="Коммерческое помещение",
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Изображение Коммерческого помещения"
        verbose_name_plural = "Изображения Коммерческого помещения"


class FloorPlansCommercialPremises(models.Model):
    """Модель Планировка Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="Описание, alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Планировка Коммерческого помещения")
    commercial_premises = models.ForeignKey(CommercialPremises, verbose_name="Коммерческое помещение",
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Планировка Коммерческого помещения"
        verbose_name_plural = "Планировки Коммерческого помещения"
