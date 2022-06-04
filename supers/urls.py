from django.urls import path 
from . import views

urlspatterns = [
    path('heroes-villains/', views.super_types)
]