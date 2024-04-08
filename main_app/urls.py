from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]