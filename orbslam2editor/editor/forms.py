from django import forms
from django.core.validators import FileExtensionValidator


class FileUploadForm(forms.Form):   #Django中用於定義標準表單的基類
    csv_file = forms.FileField(
        label='CSV File',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'})
    )
    video_file = forms.FileField(
        label='Video File',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'})
    )

