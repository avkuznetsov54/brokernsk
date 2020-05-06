from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (District, Deadline, Developer, ClassOfHousing,
                     BusinessCategory, PurposeOfCommercialPremise, CookerHood, TypeEntranceToCommercialPremises,
                     CommunicationSystems, FloorInBuilding, RelativeLocation, ResidentialComplex, CommercialPremises,
                     ImagesResidentialComplex, ImagesCommercialPremises, FloorPlansCommercialPremises,
                     NamesOfMetroStations, MaterialWallsOfHouse, City, Region, ApartmentDecoration, Infrastructure,
                     NumberOfRooms, ResidentialPremise, FloorPlansResidentialPremise, VideoResidentialComplex)


class ImagesResidentialComplexInline(admin.TabularInline):
    model = ImagesResidentialComplex
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


class ImagesCommercialPremisesInline(admin.TabularInline):
    model = ImagesCommercialPremises
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


class FloorPlansCommercialPremisesInline(admin.TabularInline):
    model = FloorPlansCommercialPremises
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


@admin.register(NumberOfRooms)
class NumberOfRoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subname')
    list_display_links = ('name',)


@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_date', 'only_year', 'only_quarter')
    list_display_links = ('full_date',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ClassOfHousing)
class ClassNewBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ImagesResidentialComplex)
class ImagesResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(ImagesCommercialPremises)
class ImagesCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(FloorPlansCommercialPremises)
class FloorPlansCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(FloorPlansResidentialPremise)
class FloorPlansResidentialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(PurposeOfCommercialPremise)
class PurposeOfCommercialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CookerHood)
class CookerHoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(TypeEntranceToCommercialPremises)
class TypeEntranceToCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CommunicationSystems)
class CommunicationSystemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(FloorInBuilding)
class FloorInBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_floor')
    list_display_links = ('num_floor',)


@admin.register(RelativeLocation)
class RelativeLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(NamesOfMetroStations)
class NamesOfMetroStationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'distance_to_center')
    list_display_links = ('name',)


@admin.register(MaterialWallsOfHouse)
class MaterialWallsOfHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ApartmentDecoration)
class ApartmentDecorationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(ResidentialComplex)
class ResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'developer', 'is_active')
    list_display_links = ('name',)
    list_filter = ('is_active', 'developer',)
    search_fields = ('name', 'address', 'developer',)
    inlines = [ImagesResidentialComplexInline]
    save_on_top = True
    save_as = True
    list_editable = ("is_active",)


@admin.register(CommercialPremises)
class CommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'district', 'area', 'is_sale', 'is_rent', 'is_active')
    list_display_links = ('address',)
    list_filter = ('is_active', 'is_sale', 'is_rent', 'district',)
    search_fields = ("address",)
    inlines = [ImagesCommercialPremisesInline, FloorPlansCommercialPremisesInline]
    save_on_top = True
    save_as = True
    list_editable = ("is_active",)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            'fields': ('is_active',
                       ('is_sale', 'is_rent'),),
        }),
        (None, {
            'fields': ('area',
                       'min_area',
                       'max_area',
                       ('floor', 'several_floors'),
                       'region',
                       'city',
                       'address',
                       'district',
                       'relative_location',
                       'residential_complex',
                       'ready_commercial_premise',
                       'purpose_commercial_premise',
                       'business_category',
                       ),
        }),
        (None, {
            'fields': ('rent_price',
                       'cost_of_sale',
                       'min_payback',
                       'max_payback',
                       'min_average_rental_rate',
                       'max_average_rental_rate',
                       'possible_income',
                       ),
        }),
        (None, {
            'fields': ('kw',
                       'min_kw',
                       'max_kw',
                       'communication_systems',
                       'cooker_hood',
                       'type_entrance',
                       ),
        }),
        (None, {
            'fields': ('description',
                       ),
        }),
        (None, {
            'fields': ('longitude',
                       'latitude',
                       ),
        }),
        (None, {
            'fields': ('alt_attr',
                       ('main_image', 'get_image'),
                       ),
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} height="70"')

    get_image.short_description = ''


@admin.register(ResidentialPremise)
class ResidentialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_rooms', 'area', 'price', 'res_complex', 'is_active')
    list_display_links = ('id',)


@admin.register(VideoResidentialComplex)
class VideoResidentialComplexAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_on_video', 'residential_complex')
    list_display_links = ('id',)


admin.site.site_title = "BROKERNSK.PRO"
admin.site.site_header = "BROKERNSK.PRO"
