from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ''}))
    search_from = forms.DateField(
        widget=DateInput(attrs={'value': datetime.date.today}))
    search_to = forms.DateField(
        widget=DateInput())
