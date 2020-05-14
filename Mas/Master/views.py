from django.shortcuts import redirect, render

from . import forms

from .backend.Master import nsdl, cdsl
from django.http import HttpResponse, JsonResponse

# Create your views here.



def index(request):
    return render(request, 'Master/index.html')


def nsdlbenpos(request):

    if request.method == 'POST':

        form = forms.NSDLForm(request.POST, request.FILES)

        if form.is_valid():
            print("Here")
            return JsonResponse(
                nsdl.main(form.cleaned_data.get('filepath')
                          )
                )

        else:
            return HttpResponse("<h1> Bad File Error </h1>")


    form=forms.NSDLForm()
    return render(request, 'Master/nsdlbenpos.html', context={"form": form})


def cdslbenpos(request):
    return render(request, 'Master/cdslbenpos.html')
