from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['account']

    # image1 = forms.ImageField(label="Car Image 1 *")
    # image2 = forms.ImageField(label="Car Image 2", required=False)
    # image3 = forms.ImageField(label="Car Image 3", required=False)
    # image4 = forms.ImageField(label="Car Image 4", required=False)
    # image5 = forms.ImageField(label="Car Image 5", required=False)
