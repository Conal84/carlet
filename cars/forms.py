from django import forms
from .models import Car
from .widgets import CustomClearableFileInput


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['location'].widget = forms.TextInput(attrs={
            'id': 'search-location',
        })

    image1 = forms.ImageField(label="Car Image 1 *", widget=CustomClearableFileInput)
    image2 = forms.ImageField(label="Car Image 2", required=False, widget=CustomClearableFileInput)
    image3 = forms.ImageField(label="Car Image 3", required=False, widget=CustomClearableFileInput)
