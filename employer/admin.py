from django.contrib import admin
from .models import *
from.forms import HireForInlineForm


# Register your models here.
class HireForInline(admin.TabularInline):
    model = HireFor
    extra = 1
    form = HireForInlineForm


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'birth_date',
        'contact_number', 'aadhar_number', )
    list_display_links = ('id', )
    search_fields = ('full_name', )
    list_filter = ('gender', 'contact_verified', )
    list_per_page = 50
    raw_id_fields = ('address', 'user', )
    inlines = [HireForInline]


class HireForAdmin(admin.ModelAdmin):
    form = HireForInlineForm
    list_display = (
        'id', 'profile', 'employment_type',
        'designation', 'desired_Job_type', )
    list_display_links = ('id', )
    search_fields = ('profile__full_name', )
    list_filter = ('desired_Job_type', 'employment_type', )
    list_per_page = 50


admin.site.register(Profile,  ProfileAdmin)
admin.site.register(HireFor,  HireForAdmin)
