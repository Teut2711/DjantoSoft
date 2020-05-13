from django import forms
# Create your forms here.


class NSDLForm(forms.Form):
    filepath = forms.FileField(widget=forms.FileInput(attrs={"accept":".txt"}) , label="Select File ", required=True)