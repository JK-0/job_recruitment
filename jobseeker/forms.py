from django import forms
from .models import Profile, Employment, CareerProfile
from job.models import Education
from dal import autocomplete


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('date_created', 'date_updated', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmploymentInlineForm(forms.ModelForm):
    class Meta:
        model = Employment
        exclude = ('date_created', 'date_updated', )
        widgets = {
            'designation': autocomplete.ModelSelect2(url='designation-autocomplete'),
            'skill': autocomplete.ModelSelect2Multiple(url='key-skill-autocomplete')
        }

    class Media:
        css = {
            'all': ('select2_custom.css',),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EducationInlineForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('__all__')
        exclude = ('job', )

        widgets = {
            'university': autocomplete.ModelSelect2(
                url='university-autocomplete',
                attrs={
                    # Set some placeholder
                    # 'data-placeholder': 'Autocomplete ...',
                    # Only trigger autocompletion after 3 characters have been typed
                    'data-minimum-input-length': 1,
                    'class': '',
                },
                ),
            'course_name': autocomplete.ModelSelect2(
                url='course-name-autocomplete',
                forward=['education_type'],
                ),
            'specialization': autocomplete.ModelSelect2(
                url='specialization-autocomplete',
                forward=['course_name'],
                ),
        }

    class Media:
        css = {
            'all': ('select2_custom.css',),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CareerProfileInlineForm(forms.ModelForm):
    class Meta:
        model = CareerProfile
        exclude = ('date_created', 'date_updated', )
        widgets = {
            'role': autocomplete.ModelSelect2(
                url='role-autocomplete',
                forward=['functional_area'],
                ),
        }

    class Media:
        css = {
            'all': ('select2_custom.css',),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
