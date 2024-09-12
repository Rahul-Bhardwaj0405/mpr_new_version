from django import forms

class FileUploadForm(forms.Form):
    folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
