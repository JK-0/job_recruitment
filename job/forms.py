from django import forms
from .models import Education, Job
from dal import autocomplete


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('__all__')
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


class EducationInlineForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('__all__')
        exclude = ('jobseeker', )

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


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('date_created', 'date_updated', )
        widgets = {
            'designation': autocomplete.ModelSelect2(url='designation-autocomplete'),
            'skill': autocomplete.ModelSelect2Multiple(url='key-skill-autocomplete'),
            'role': autocomplete.ModelSelect2(url='role-autocomplete', forward=['functional_area'],),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
