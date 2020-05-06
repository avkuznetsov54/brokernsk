from django.db import models
import datetime


# ф-ция генерит путь для загружаемого изображения и планировок
def generate_url_for_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


# ф-ция генерит путь для загружаемого логотипа застройщика
def generate_url_for_logo_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/logo_image/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
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


class Deadline(models.Model):
    """Модель Срок сдачи"""
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
    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип застройщика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class ClassOfHousing(models.Model):
    """Модель Класс Жилья"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Жилья'
        verbose_name_plural = 'Классы Жилья'
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
    """Модель Этаж"""
    num_floor = models.IntegerField(db_index=True, verbose_name='Этаж')

    def __str__(self):
        return f'{self.num_floor}'

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'
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


class NamesOfMetroStations(models.Model):
    """Модель Метро"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    distance_to_center = models.CharField(max_length=50, null=True, blank=True, verbose_name='Расстояние до центра')
    sub_text_distance_to_center = models.CharField(max_length=255, null=True, blank=True,
                                                   verbose_name='Текс для тултипа')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'
        ordering = ['name']


class MaterialWallsOfHouse(models.Model):
    """Модель Материал стен дома"""
    name = models.CharField(max_length=255, unique=True, verbose_name='Материал стен дома')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал стен дома'
        verbose_name_plural = 'Материалы стен дома'
        ordering = ['name']


class City(models.Model):
    """Модель Город"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение Города")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class Region(models.Model):
    """Модель Область"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'
        ordering = ['name']


class ApartmentDecoration(models.Model):
    """Модель Отделка квартиры"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка квартиры'
        verbose_name_plural = 'Отделки квартиры'
        ordering = ['name']


class Infrastructure(models.Model):
    """Модель Инфраструктура"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    icon = models.FileField(upload_to=generate_url_for_image,
                            null=True,
                            blank=True,
                            verbose_name="Иконка")
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'
        ordering = ['name']


class NumberOfRooms(models.Model):
    """Модель Количество комнат"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'
        ordering = ['name']


class ResidentialComplex(models.Model):
    """Модель Жилого Комплекса"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Название ЖК')

    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип ЖК")

    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Застройщик',
                                  related_name="rescomplex_developer",
                                  default=None,
                                  null=True,
                                  blank=True)
    class_of_housing = models.ForeignKey(ClassOfHousing,
                                         on_delete=models.SET_NULL,
                                         verbose_name='Класс Новостройки',
                                         related_name='rescomplex_classofhousing',
                                         default=None,
                                         null=True,
                                         blank=True)
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='rescomplex_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='rescomplex_city',
                             default=None,
                             null=True,
                             blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='rescomplex_district',
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
    deadline = models.ManyToManyField(Deadline,
                                      verbose_name='Срок сдачи',
                                      related_name='rescomplex_deadline',
                                      default=None,
                                      blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение ЖК")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    distance_to_metro = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Растояние до метро, м')
    metro_stations = models.ManyToManyField(NamesOfMetroStations,
                                            verbose_name='Название ближайщего метро',
                                            related_name='rescomplex_metrostations',
                                            default=None,
                                            blank=True)

    site_developer = models.URLField(max_length=300,
                                     verbose_name='Сайт застройщика/Жилого комплекса',
                                     default=None,
                                     null=True,
                                     blank=True)

    infrastructure = models.ManyToManyField(Infrastructure,
                                            verbose_name='Инфраструктура',
                                            related_name='rescomplex_infrastructure',
                                            default=None,
                                            blank=True)
    material_walls = models.ManyToManyField(MaterialWallsOfHouse,
                                            verbose_name='Материал стен дома',
                                            related_name='rescomplex_materialwalls',
                                            default=None,
                                            blank=True)
    apart_decoration = models.ManyToManyField(ApartmentDecoration,
                                              verbose_name='Отделка',
                                              related_name='rescomplex_apartdecoration',
                                              default=None,
                                              blank=True)
    is_visible_video = models.BooleanField(default=False, verbose_name='Показывать видео')

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

    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='compremises_floor',
                                   default=None,
                                   blank=True)

    several_floors = models.BooleanField(default=False, verbose_name='Помещение с несколькими этажами')

    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='compremises_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='compremises_city',
                             default=None,
                             null=True,
                             blank=True)
    address = models.CharField(max_length=150, db_index=True, default=None, verbose_name='Адрес')
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='compremises_district',
                                 default=None,
                                 null=True,
                                 blank=True)
    relative_location = models.ManyToManyField(RelativeLocation,
                                               verbose_name='Расположение',
                                               related_name='compremises_relativelocation',
                                               default=None,
                                               blank=True)

    residential_complex = models.ForeignKey(ResidentialComplex,
                                            on_delete=models.SET_NULL,
                                            verbose_name='Жилой комплекс',
                                            related_name='compremises_rescomplex',
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
                                                        related_name='compremises_purpose',
                                                        default=None,
                                                        blank=True)
    business_category = models.ManyToManyField(BusinessCategory,
                                               verbose_name='Категория бизнеса',
                                               related_name='compremises_businesscategory',
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
                                                   related_name='compremises_comsystems',
                                                   default=None,
                                                   blank=True)
    cooker_hood = models.ForeignKey(CookerHood,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Вытяжка',
                                    related_name='compremises_cookerhood',
                                    default=None,
                                    null=True,
                                    blank=True)
    type_entrance = models.ManyToManyField(TypeEntranceToCommercialPremises,
                                           verbose_name='Тип входа',
                                           related_name='compremises_typeentrance',
                                           default=None,
                                           blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение помещения")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Коммерческое помещение'
        verbose_name_plural = 'Коммерческие помещения'
        # ordering = ['name']


class ResidentialPremise(models.Model):
    """Модель Жилого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    res_complex = models.ForeignKey(ResidentialComplex,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Жилой комплекс',
                                    related_name='respremises_rescomplex',
                                    default=None,
                                    null=True,
                                    blank=True)
    number_rooms = models.ForeignKey(NumberOfRooms,
                                     on_delete=models.SET_NULL,
                                     verbose_name='Количество комнат',
                                     related_name='respremises_numberrooms',
                                     default=None,
                                     null=True)

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена')
    min_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена от, м')
    max_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена до, м')

    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='respremises_floor',
                                   default=None,
                                   blank=True)

    # def __str__(self):
    #     return self.number_rooms

    class Meta:
        verbose_name = 'Жилое помещение'
        verbose_name_plural = 'Жилые помещения'
        # ordering = ['name']


class ImagesResidentialComplex(models.Model):
    """Модель Изображение Жилого Комплекса"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
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


class FloorPlansResidentialPremise(models.Model):
    """Модель Планировка Жилого помещения"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Планировка Жилого помещения")

    residential_premises = models.ForeignKey(ResidentialPremise, verbose_name="Жилое помещение",
                                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Планировка Жилого помещения"
        verbose_name_plural = "Планировки Жилого помещения"


class ImagesCommercialPremises(models.Model):
    """Модель Изображение Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
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
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
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


class VideoResidentialComplex(models.Model):
    """Модель Видео Жилого Комплекса"""
    link_on_video = models.URLField(max_length=2000,
                                    verbose_name='Ссылка на видео',
                                    default=None,
                                    null=True,
                                    blank=True)
    residential_complex = models.ForeignKey(ResidentialComplex, verbose_name="Жилой Комплекс", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Видео Жилого Комплекса'
        verbose_name_plural = 'Видео Жилого Комплекса'
        ordering = ['id']
