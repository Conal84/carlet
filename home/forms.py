from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from datetime import date


today = date.today()


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Location'}), label=False
    )
    search_from = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "YYYY-MM-DD",
            }),
        label=False
    )
    search_to = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "YYYY-MM-DD",
            }),
        label=False
    )
