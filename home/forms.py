from django import forms
import datetime


class SearchForm(forms.Form):
    location = forms.CharField()
    hire_from = forms.DateField(initial=datetime.date.today)
    hire_to = forms.DateField()
