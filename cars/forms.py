from django import forms
from .models import Car
from .widgets import CustomClearableFileInput


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['user']

    image1 = forms.ImageField(label="Car Image 1 *", widget=CustomClearableFileInput)
    image2 = forms.ImageField(label="Car Image 2", required=False, widget=CustomClearableFileInput)
    image3 = forms.ImageField(label="Car Image 3", required=False, widget=CustomClearableFileInput)
    image4 = forms.ImageField(label="Car Image 4", required=False, widget=CustomClearableFileInput)
    image5 = forms.ImageField(label="Car Image 5", required=False, widget=CustomClearableFileInput)
