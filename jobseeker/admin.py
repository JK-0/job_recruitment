from django.contrib import admin
from job.models import Education
from .models import *
from .forms import ProfileForm, EmploymentInlineForm, EducationInlineForm, CareerProfileInlineForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


# Register your models here.
class EmploymentInline(admin.TabularInline):
    model = Employment
    extra = 1
    form = EmploymentInlineForm
    # filter_horizontal = ('skill',)

    # prepopulated_fields = {'asset_slug': ('name',)}
    # fields = ['asset_file', 'name', 'asset_slug', ]
    # exclude = ['created_by', ]


class EducationInline(admin.TabularInline):
    model = Education
    form = EducationInlineForm
    extra = 1


class CareerProfileInline(admin.TabularInline):
    model = CareerProfile
    form = CareerProfileInlineForm
    extra = 1
    # filter_horizontal = ('language',)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1


class PaperResearchPublicationInline(admin.TabularInline):
    model = PaperResearchPublication
    extra = 1


class WorkSampleInline(admin.TabularInline):
    model = WorkSample
    extra = 1


class KnownLanguageInline(admin.TabularInline):
    model = KnownLanguage
    extra = 1


class ProfileResource(resources.ModelResource):
    user = Field(
                column_name='user',
                attribute='user',
                widget=ForeignKeyWidget(User, 'email'))
    follow = Field(
                column_name='follow',
                attribute='follow',
                widget=ManyToManyWidget(EmployerProfile, field='full_name'))

    class Meta:
        model = Profile
        import_id_fields = ('id',)
        fields = (
            'id',
            'user',
            'full_name',
            'gender',
            'marital_status',
            'birth_date',
            'contact_number',
            'contact_verified',
            'resume_file',
            'profile_pic',
            'resume_headline',
            'profile_summary',
            'aadhar_number',
            'aadhar_verified',
            'pan_number',
            'pan_verified',
            'annual_salary_in_lac',
            'annual_salary_in_thousand',
            'annual_salary',
            'linked_in_profile',
            'twitter_profile',
            'youtube_profile',
            'facebook_profile',
            'instagram_profile',
            'webpage_link',
            'other_link',
            'follow',
            'date_created',
            'date_updated',
            'complete_profile_percentage',
            'address',
        )
        export_order = (
            'id',
            'user',
            'full_name',
            'gender',
            'marital_status',
            'birth_date',
            'contact_number',
            'contact_verified',
            'resume_file',
            'profile_pic',
            'resume_headline',
            'profile_summary',
            'aadhar_number',
            'aadhar_verified',
            'pan_number',
            'pan_verified',
            'annual_salary_in_lac',
            'annual_salary_in_thousand',
            'annual_salary',
            'linked_in_profile',
            'twitter_profile',
            'youtube_profile',
            'facebook_profile',
            'instagram_profile',
            'webpage_link',
            'other_link',
            'follow',
            'date_created',
            'date_updated',
            'complete_profile_percentage',
            'address',
        )


class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    form = ProfileForm
    list_display = (
        'id', 'full_name', 'marital_status', 'birth_date',
        'contact_number', 'aadhar_number', )
    list_display_links = ('id', )
    search_fields = (
        'full_name', )
    list_filter = ('gender', 'marital_status',
                   'contact_verified', 'annual_salary_in_lac', )
    list_per_page = 50
    filter_horizontal = ('follow',)
    raw_id_fields = ('address', 'user',)
    inlines = [
        EmploymentInline,
        EducationInline,
        CareerProfileInline,
        ProjectInline,
        CertificationInline,
        PaperResearchPublicationInline,
        WorkSampleInline,
        KnownLanguageInline
    ]


class EmploymentAdmin(admin.ModelAdmin):
    form = EmploymentInlineForm
    list_display = ('id', 'profile', 'company_name',
                    'employment_type', 'designation', 'website_link', )
    list_display_links = ('id', )
    search_fields = ('company_name', 'profile__full_name', )
    list_filter = ('employment_type', )
    list_per_page = 100
    filter_horizontal = ('skill',)


class CareerProfileAdmin(admin.ModelAdmin):
    form = CareerProfileInlineForm
    list_display = ('id', 'desired_Job_type',
                    'desired_employment_type', 'preferred_shift', )
    list_display_links = ('id', )
    search_fields = ('desired_Job_type',
                     'desired_employment_type', 'preferred_shift', )
    list_filter = ('desired_Job_type',
                   'desired_employment_type', 'preferred_shift', )
    list_per_page = 100


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_title', 'project_status',
                    'project_start_year', 'project_link', )
    list_display_links = ('id', )
    search_fields = ('project_title', )
    list_filter = ('project_status', )
    list_per_page = 100


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'certification_name',
                    'certified_by', 'certificate_link', )
    list_display_links = ('id', )
    search_fields = ('certification_name', )
    list_filter = ('certified_by', )
    list_per_page = 100


class PaperResearchPublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'web_link', 'published_year', )
    list_display_links = ('id', )
    search_fields = ('title', )
    list_filter = ('published_year', )
    list_per_page = 100


class WorkSampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'web_link',
                    'start_year', 'status', 'end_year',)
    list_display_links = ('id', )
    search_fields = ('title', )
    list_filter = ('status', 'start_year')
    list_per_page = 100


class KnownLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'language',
                    'can_read', 'can_write', 'can_speak',)
    list_display_links = ('id', )
    search_fields = ('profile', )
    list_filter = ('can_read', 'can_write', 'can_speak')
    list_per_page = 100


admin.site.register(Profile,  ProfileAdmin)
admin.site.register(Employment,  EmploymentAdmin)
admin.site.register(CareerProfile,  CareerProfileAdmin)
admin.site.register(Project,  ProjectAdmin)
admin.site.register(Certification,  CertificationAdmin)
admin.site.register(PaperResearchPublication,  PaperResearchPublicationAdmin)
admin.site.register(WorkSample,  WorkSampleAdmin)
admin.site.register(KnownLanguage,  KnownLanguageAdmin)
