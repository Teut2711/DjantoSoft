from django import forms
from django.core.mail import send_mail
from .mailer import Mailer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions

import json
from django.http import JsonResponse

class EmailForm(forms.Form):

    host = forms.CharField(max_length=30)
    username = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=5)
    file_excel = forms.FileField(label="File to upload")
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Upload File',
                'host',
                'username',
                'password',
                'file_excel',
                ),
            FormActions(
                Submit('submit', 'Submit'),
            )
        )

    def send_email(self):
        mailer = Mailer(**self.cleaned_data)
        return mailer.send_mail()
    

    def save(self):
        pass