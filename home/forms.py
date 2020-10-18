from django import forms
import datetime


class SearchForm(forms.Form):
    location = forms.CharField(initial="Search by Location")
    hire_from = forms.DateField(initial=datetime.date.today)
    hire_to = forms.DateField(initial="Hire To")
