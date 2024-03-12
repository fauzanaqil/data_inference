# display_data_project/data_processor/forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
