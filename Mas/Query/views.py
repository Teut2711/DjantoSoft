from django.shortcuts import render

# Create your views here.

import os
import pathlib
import base64

PATH = pathlib.Path(__file__).parent

def img_process(img_obj):
    print(dir(img_obj))
    encoded_string = base64.b64encode(img_obj.read())
    return encoded_string

def index(request):
    if request.method == "POST":
    


           
        return render(request, "Query\index.html", context={
            "img_mine":
                f"data:{request.FILES['filepath'].content_type};base64," +
                 img_process(
                request.FILES['filepath']
                ).decode()
        })  

        
    return render(request, "Query\index.html", context={
            "img_mine": 
                 ""
                })
    
