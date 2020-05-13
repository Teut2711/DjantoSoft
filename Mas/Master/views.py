from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
# Create your views here.

from . import forms

from .backend.Master import nsdl, cdsl


def index(request):
    return render(request, 'Master/index.html')


def nsdlbenpos(request):

    if request.method == 'POST':
        
        form = forms.NSDLForm(request.POST, request.FILES)

        if form.is_valid():

            nsdl.main(form.cleaned_data.get('filepath'))

            return HttpResponse("<h1>Process Completed</h1>")
        else:
            return HttpResponse("<h1>Bad File Input</h1>")
 

    form = forms.NSDLForm()
    return render(request, 'Master/nsdlbenpos.html', context={"form": form})


def cdslbenpos(request):
    return render(request, 'Master/cdslbenpos.html')
