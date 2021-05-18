from django.shortcuts import render


def home_page_view(request):
    return render(request, 'website/home.html')


def alexa_page_view(request):
    return render(request, 'website/alexa.html')


def aspirador_page_view(request):
    return render(request, 'website/aspirador.html')


def bimby_page_view(request):
    return render(request, 'website/bimby.html')
