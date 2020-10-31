from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ''}))
    hire_from = forms.DateField(
        widget=DateInput(attrs={'value': datetime.date.today}))
    hire_to = forms.DateField(
        widget=DateInput())
