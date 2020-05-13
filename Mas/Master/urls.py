from django.urls import path
from . import views

urlpatterns = [
    path("Master/", views.index, name="Master-index"),
    path("Master/nsdlbenpos/", views.nsdlbenpos, name="Master-nsdlbenpos"),
    path("Master/cdslbenpos/", views.cdslbenpos, name="Master-cdslbenpos"),
]
