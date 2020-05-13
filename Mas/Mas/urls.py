from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Base.urls")),
    path("", include("Master.urls")),
    path("", include("Email.urls")),
]
