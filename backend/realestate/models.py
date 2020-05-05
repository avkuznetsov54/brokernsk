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
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class ClassNewBuilding(models.Model):
    """Модель Класс Новостройки"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Новостройки'
        verbose_name_plural = 'Классы Новостроек'
        ordering = ['name']


class ImagesRealEstate(models.Model):
    """Модель Изображение"""
    alt_attr = models.TextField("Описание, alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             blank=True,
                             verbose_name="Изображение")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class FloorPlansRealEstate(models.Model):
    """Модель Планировка"""
    alt_attr = models.TextField("Описание, alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             blank=True,
                             verbose_name="Планировка")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Планировка"
        verbose_name_plural = "Планировки"


class BusinessCategory(models.Model):
    """Модель Категория бизнеса"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория бизнеса'
        verbose_name_plural = 'Категории бизнесов'
        ordering = ['name']


class PurposeOfCommercialPremise(models.Model):
    """Модель Назначение помещения"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Назначение помещения'
        verbose_name_plural = 'Назначении помещений'
        ordering = ['name']


class CookerHood(models.Model):
    """Модель Вытяжка"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вытяжка'
        verbose_name_plural = 'Вытяжки'
        ordering = ['name']


class TypeEntranceToCommercialPremises(models.Model):
    """Модель Тип входа в коммерческое помещение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип входа в коммерческое помещение'
        verbose_name_plural = 'Типы входов в коммерческое помещение'
        ordering = ['name']


class CommunicationSystems(models.Model):
    """Модель Системы коммуникаций"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

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
        return self.num_floor

    class Meta:
        verbose_name = 'Этаж в здании'
        verbose_name_plural = 'Этажи в здании'
        ordering = ['num_floor']


class RelativeLocation(models.Model):
    """Модель Относительное расположение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Относительное расположение'
        verbose_name_plural = 'Относительные расположения'
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
                                 related_name='district',
                                 default=None,
                                 null=True,
                                 blank=True)
    address = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Адрес',
                               default=None,
                               null=True, blank=True)
    one_or_many_buildings = models.BooleanField(default=True, verbose_name='Одно/несколько строений')
    number_of_storeys = models.CharField(max_length=10, verbose_name='Этажность')
    house_completed = models.BooleanField(default=False, verbose_name='Дом сдан, Да/Нет')
    deadline = models.ManyToManyField(DeadlineNewBuilding,
                                      verbose_name='Срок сдачи',
                                      related_name='deadline',
                                      default=None,
                                      blank=True,
                                      null=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  blank=True,
                                  verbose_name="Главное изображение ЖК")
    other_images = models.ManyToManyField(ImagesRealEstate,
                                          verbose_name='Остальные изображения ЖК',
                                          related_name='otherimagesresidentialcomplex',
                                          default=None,
                                          blank=True,
                                          null=True)

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(verbose_name='Описание')

    distance_to_metro = models.IntegerField(db_index=True, verbose_name='Растояние до метро, м')

    site_developer = models.URLField(max_length=300,
                                     verbose_name='Сайт застройщика/Новостройки',
                                     default=None,
                                     null=True, blank=True)

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
    floor = models.IntegerField(db_index=True, verbose_name='Этаж')
    address = models.CharField(max_length=150, db_index=True, verbose_name='Адрес',
                               default=None,
                               null=True, blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='district',
                                 default=None,
                                 null=True,
                                 blank=True)
    relative_location = models.ForeignKey(RelativeLocation,
                                          on_delete=models.SET_NULL,
                                          verbose_name='Относительное расположение',
                                          related_name='relativelocation',
                                          default=None,
                                          null=True,
                                          blank=True)

    residential_complex = models.ForeignKey(ResidentialComplex,
                                            on_delete=models.SET_NULL,
                                            verbose_name='Жилой комплекс',
                                            related_name='residentialcomplex',
                                            default=None,
                                            null=True,
                                            blank=True)
    building_commercial_premise = models.BooleanField(default=False, verbose_name='Строящее помещение, Да/Нет')
    finished_commercial_premise = models.BooleanField(default=False, verbose_name='Готовое  помещение, Да/Нет')
    purpose_commercial_premise = models.ManyToManyField(PurposeOfCommercialPremise,
                                                        verbose_name='Назначение коммерческого помещения',
                                                        related_name='purposecommercialpremise',
                                                        default=None,
                                                        blank=True,
                                                        null=True)
    business_category = models.ManyToManyField(BusinessCategory,
                                               verbose_name='Категория бизнеса',
                                               related_name='businesscategory',
                                               default=None,
                                               blank=True,
                                               null=True)
    rent_price = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Стоимость аренды, руб/мес.')
    cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Стоймость на продажу')
    min_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость, от')
    max_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость, до')
    min_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка, от')
    max_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка, до')
    possible_income = models.IntegerField(db_index=True, verbose_name='Возможный доход')
    min_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, от')
    max_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, до')
    communication_systems = models.ManyToManyField(CommunicationSystems,
                                                   verbose_name='Системы коммуникаций',
                                                   related_name='communicationsystems',
                                                   default=None,
                                                   blank=True,
                                                   null=True)
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
                                           blank=True,
                                           null=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  blank=True,
                                  verbose_name="Главное изображение помещения")
    other_images = models.ManyToManyField(ImagesRealEstate,
                                          verbose_name='Остальные изображения помещения',
                                          related_name='otherimagescommercialpremises',
                                          default=None,
                                          blank=True,
                                          null=True)
    floor_plans = models.ManyToManyField(FloorPlansRealEstate,
                                         verbose_name='Планировки',
                                         related_name='floorplans',
                                         default=None,
                                         blank=True,
                                         null=True)
    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(verbose_name='Описание')
