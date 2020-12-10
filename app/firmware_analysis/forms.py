from django import forms

class UploadFirmwareForm(forms.Form):
    firmware = forms.FileField()