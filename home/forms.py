from django import forms
import datetime


class SearchForm(forms.Form):
    location = forms.CharField(
        label="Location", blank=False, initial="Search by Location")
    hire_from = forms.DateField(
        label="Hire from", blank=False, initial=datetime.date.today)
    hire_to = forms.DateField(label="Hire to", blank=False)
