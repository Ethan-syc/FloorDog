from django import forms
from upload.models import UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        exclude = ()