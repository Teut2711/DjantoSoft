from django.shortcuts import render
from django.views.generic.edit import FormView
from . import forms
from django.http import FileResponse, JsonResponse
from io import BytesIO
# Create your views here.


class EmailView(FormView):
    template_name = 'Email/index.html'
    form_class = forms.EmailForm
    
    def form_valid(self, form):
        response = JsonResponse(*form.send_email(),safe=False)
        response['Content-Disposition'] = 'attachment; filename="logs.json"'

        return response
