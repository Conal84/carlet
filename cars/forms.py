from django import forms
from .models import Car, CarImage


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['account']


class ImageForm(forms.ModelForm):

    class Meta:
        model = CarImage
        exclude = ['car']
