from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '',
                                      'name': 'loc'
                                      }))
    hire_from = forms.DateField(
        widget=DateInput(attrs={'value': datetime.date.today,
                                'name': 'from'
                                }))
    hire_to = forms.DateField(
        widget=DateInput(attrs={'name': 'to'
                                }))
