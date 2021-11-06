from django.shortcuts import render
from dal import autocomplete
from .models import *
import collections
from django.db.models import F
from django.core.exceptions import ImproperlyConfigured

# Create your views here.


class KeySkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return KeySkill.objects.none()

        qs = KeySkill.objects.all()

        if self.q:
            qs = qs.filter(skill__istartswith=self.q)

        return qs


class UniversityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return University.objects.none()

        qs = University.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class CourseNameAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Course.objects.none()

        qs = Course.objects.none()

        education_type = self.forwarded.get('education_type', None)

        if education_type:
            qs = Course.objects.all()
            qs = qs.filter(education_type=education_type)

        if self.q:
            qs = qs.filter(course_name__istartswith=self.q)

        return qs


class SpecializationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Specialization.objects.none()

        qs = Specialization.objects.none()

        course_name = self.forwarded.get('course_name', None)

        if course_name:
            qs = Specialization.objects.all()
            qs = qs.filter(course_name=course_name)

        if self.q:
            qs = qs.filter(specialization__istartswith=self.q)

        return qs


class Select2GroupQuerySetView(autocomplete.Select2QuerySetView):

    group_by_related = None
    related_field_name = 'name'

    def get_results(self, context):

        if not self.group_by_related:
            raise ImproperlyConfigured("Missing group_by_related.")

        groups = collections.OrderedDict()

        object_list = context['object_list']

        object_list = object_list.annotate(
            group_name=F(f'{self.group_by_related}'))

        for result in object_list:
            group_name = getattr(result, 'group_name')
            groups.setdefault(group_name, [])
            groups[group_name].append(result)

        return [{
            'id': None,
            'text': group,
            'children': [{
                'id': result.id,
                'text': getattr(result, self.related_field_name),

                # this is the line I had to comment out
                # 'title': result.descricao
            } for result in results]
        } for group, results in groups.items()]


# role with group
# reference https://stackoverflow.com/questions/65178429/how-to-mix-two-queries-to-one-as-dropdown-elements
class RoleAutocomplete(Select2GroupQuerySetView):

    group_by_related = 'role_group'  # this is the fieldname of ForeignKey
    # this is the fieldname that you want to show.
    related_field_name = 'role_name'

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Role.objects.none()

        qs = Role.objects.none()

        functional_area = self.forwarded.get('functional_area', None)

        if functional_area:
            qs = Role.objects.all()
            qs = qs.filter(functional_area=functional_area)

        if self.q:
            qs = qs.filter(role_name__istartswith=self.q)

        return qs


# role without group
# class RoleAutocomplete(autocomplete.Select2QuerySetView):

#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated:
#             return Role.objects.none()

#         qs = Role.objects.none()

#         functional_area = self.forwarded.get('functional_area', None)

#         if functional_area:
#             qs = Role.objects.all()
#             qs = qs.filter(functional_area=functional_area)

#         if self.q:
#             qs = qs.filter(role_name__istartswith=self.q)

#         return qs


class DesignationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Designation.objects.none()

        qs = Designation.objects.all()

        if self.q:
            qs = qs.filter(designation__istartswith=self.q)

        return qs


class StateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return State.objects.none()

        qs = State.objects.none()

        country = self.forwarded.get('country', None)

        if country:
            qs = State.objects.all()
            qs = qs.filter(country=country)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return City.objects.none()

        qs = City.objects.none()

        state = self.forwarded.get('state', None)

        if state:
            qs = City.objects.all()
            qs = qs.filter(state=state)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
