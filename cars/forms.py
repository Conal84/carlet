from django import forms
from .models import Car
from .widgets import CustomClearableFileInput


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['user']
        widgets = {
          'description': forms.Textarea(attrs={'rows': 3,
                                               'cols': 10,
                                               'style': 'height: 12rem;'
                                               }),
        }

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget = forms.TextInput(attrs={
            'id': 'search-location',
        })
        self.fields['available_from'].widget = forms.TextInput(attrs={
            'id': 'search-from',
        })
        self.fields['available_to'].widget = forms.TextInput(attrs={
            'id': 'search-to',
        })
        self.fields['cost_per_day'].widget = forms.TextInput(attrs={
            'placeholder': '£',
        })

    image1 = forms.ImageField(label="", widget=CustomClearableFileInput)
    image2 = forms.ImageField(label="", required=False, widget=CustomClearableFileInput)
    image3 = forms.ImageField(label="", required=False, widget=CustomClearableFileInput)
