from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('alexa', views.alexa_page_view, name='alexa'),
    path('aspirador', views.aspirador_page_view, name='aspirador'),
    path('bimby', views.bimby_page_view, name='bimby')
]