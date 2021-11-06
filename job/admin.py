from django.contrib import admin
from .models import *
from .forms import EducationForm, EducationInlineForm, JobForm


# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    form = EducationForm
    list_display = ('id', 'education_type', 'passing_out_year', 'university', )
    list_display_links = ('id', )
    search_fields = ('university', 'education_type', 'passing_out_year', )
    list_filter = ('education_type', )
    list_per_page = 100


class EducationInline(admin.TabularInline):
    model = Education
    form = EducationInlineForm
    extra = 1


class JobAdmin(admin.ModelAdmin):
    form = JobForm
    list_display = (
        'id', 'job_title', 'functional_area', 'job_status',
        'employment_type', 'job_shift', )
    list_display_links = ('id', )
    list_filter = ('job_status', 'employment_type',
                   'job_shift', 'preferred_gender', )
    filter_horizontal = ('jobseeker',)
    search_fields = ('job_title', )
    list_per_page = 100
    raw_id_fields = ('address', 'employer', )
    inlines = [
        EducationInline,
    ]


admin.site.register(Education,  EducationAdmin)
admin.site.register(Job,  JobAdmin)
