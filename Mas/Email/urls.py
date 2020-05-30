
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('email/', views.EmailView.as_view(), name="Email-index"),
]
