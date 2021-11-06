from django import forms
from .models import HireFor
from dal import autocomplete
from dal import forward


class HireForInlineForm(forms.ModelForm):
    class Meta:
        model = HireFor
        fields = ('__all__')
        widgets = {
            'designation': autocomplete.ModelSelect2(url='designation-autocomplete'),
            'skill': autocomplete.ModelSelect2Multiple(url='key-skill-autocomplete'),
            'role': autocomplete.ModelSelect2(
                url='role-autocomplete',
                forward=['functional_area', ],
            ),
        }

    class Media:
        css = {
            'all': ('select2_custom.css',),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
