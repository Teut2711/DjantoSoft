import os
import shutil
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import subprocess as sp
sp.run("pip install poetry".split(), shell=False)
sp.run("poetry init --no-interaction --dependency django".split(), shell=False)
sp.run("poetry install".split(), shell=False)
fle = input('Enter Project name   : ')

if not os.path.exists(fle):
    sp.run(f"poetry run django-admin.py startproject {fle}".split(), shell=False)

os.chdir(fle)
Appname = input("Enter Input like this(space seperated) --> A B C D : ").strip().split()
    
for i in Appname:
    if not os.path.exists(i):
        sp.run(f"poetry run python manage.py startapp {i}".split(), shell=False)

for i in Appname:
    os.chdir(i)
    try:
        os.makedirs(f"templates/{i}")
    except  FileExistsError:
        pass
    try:
        os.makedirs(f"static/{i}")
    except FileExistsError:
        pass
    try: 
        shutil.copy(f"../{fle}/urls.py", f"urls.py", )
    except FileExistsError:
        pass
    
    with open(f"views.py", "a+") as obj:
        string = f'''
    \rdef index(request):
    \r    return render(request, "{i}/index.html")
    \r'''
        if not(string in obj.read()):
            obj.write(string)
        
    
    try:
        open(os.path.join("templates",i, "index.html") , "x")
    except FileExistsError:
         pass
    try:
        open(os.path.join("static",i, "index.css") , "x")
    
    except FileExistsError:
         pass
    try:
       open(os.path.join("static",i, "index.js") , "x")
    except FileExistsError:
         pass
    
    
    os.chdir("..")