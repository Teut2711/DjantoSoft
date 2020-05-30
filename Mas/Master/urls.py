from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Master-index"),
    path("nsdlbenpos/", views.nsdlbenpos, name="Master-nsdlbenpos"),
    path("cdslbenpos/", views.cdslbenpos, name="Master-cdslbenpos"),
]
