from django.contrib import admin
from .models import *
from .forms import AddressForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


class StateResource(resources.ModelResource):
    country = Field(
                column_name='country',
                attribute='country',
                widget=ForeignKeyWidget(Country, 'name'))

    class Meta:
        model = State
        fields = ('id', 'country', 'name', )
        exclude = ('description',)
        export_order = ('id', 'country', 'name', )
        import_id_fields = ('id',)


# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'iso2', 'iso3',
        'phone_code', 'capital', 'currency', )
    list_display_links = ('name', )
    search_fields = (
        'name', 'iso2', 'iso3',
        'phone_code', 'capital', 'currency', )
    list_filter = ('currency', )
    list_per_page = 50


class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource

    list_display = ('id', 'name', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', 'country__name', )
    list_filter = ('country', )
    list_per_page = 100


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', 'country__name', 'state__name', )
    list_filter = ('country', )
    list_per_page = 100


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domain', 'web_page', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', 'domain', 'web_page', )
    list_filter = ('country', )
    list_per_page = 100


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'board_name', 'board_type', 'verified')
    list_display_links = ('id', )
    search_fields = ('board_name', )
    list_filter = ('board_type', )
    list_per_page = 100


class SchoolMediumAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_medium', 'verified')
    list_display_links = ('id', )
    search_fields = ('school_medium', )
    list_per_page = 100


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'education_type', 'verified', )
    list_display_links = ('id', )
    search_fields = ('course_name', 'education_type', )
    list_per_page = 100


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialization', 'course_name',
                    'education_type', 'verified', )
    list_display_links = ('id', )
    search_fields = ('specialization', 'course_name__course_name', )
    list_per_page = 100


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'alpha2', 'alpha3_b', 'verified')
    list_display_links = ('id', )
    search_fields = ('language', 'alpha2', )
    list_per_page = 100


class FunctionalAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'functional_area_name', 'verified', )
    list_display_links = ('id', )
    search_fields = ('functional_area_name', )
    list_per_page = 100


class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'designation', 'verified', )
    list_display_links = ('id', )
    search_fields = ('designation', )
    list_per_page = 100


class KeySkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'verified', )
    list_display_links = ('id', )
    search_fields = ('skill', )
    list_per_page = 100


class PreferredLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'verified', )
    list_display_links = ('id', )
    search_fields = ('location', )
    list_per_page = 100


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'role_group',
                    'functional_area', 'verified', )
    list_display_links = ('id', )
    search_fields = ('role_name', 'role_group',
                     'functional_area__functional_area_name', )
    list_per_page = 100


class AddressAdmin(admin.ModelAdmin):
    form = AddressForm

    list_display = ('id', 'pin_code', 'address_one',
                    'address_two', 'address_three', )
    list_display_links = ('id', )
    search_fields = ('pin_code',)
    list_per_page = 100


admin.site.register(Country,  CountryAdmin)
admin.site.register(State,  StateAdmin)
admin.site.register(City,  CityAdmin)
admin.site.register(University,  UniversityAdmin)
admin.site.register(Board,  BoardAdmin)
admin.site.register(SchoolMedium,  SchoolMediumAdmin)
admin.site.register(Course,  CourseAdmin)
admin.site.register(Specialization,  SpecializationAdmin)
admin.site.register(Language,  LanguageAdmin)
admin.site.register(FunctionalArea,  FunctionalAreaAdmin)
admin.site.register(Designation,  DesignationAdmin)
admin.site.register(KeySkill,  KeySkillAdmin)
admin.site.register(PreferredLocation,  PreferredLocationAdmin)
admin.site.register(Role,  RoleAdmin)
admin.site.register(Address,  AddressAdmin)
