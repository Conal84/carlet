from django import forms
from .models import Car, CarImage


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['account']
        image = model.car_image


class ImageForm(forms.ModelForm):

    class Meta:
        model = CarImage
        exclude = ['car']
