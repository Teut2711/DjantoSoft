from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Base.urls")),
    path("Master/", include("Master.urls")),
    path("Email/", include("Email.urls")),
    path("Query/", include("Query.urls")),
    path("Report/", include("Report.urls")),

]
