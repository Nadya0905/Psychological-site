from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def doctors(request):
    return render(request, 'main/doctors.html')


def reviews(request):
    return render(request, 'main/reviews.html')


def register(request):
    return render(request, 'register.html')