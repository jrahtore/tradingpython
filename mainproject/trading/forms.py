
from django import forms




class DataForm(forms.Form):
    data_file = forms.FileField()