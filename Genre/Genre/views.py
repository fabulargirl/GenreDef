from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Genre/index.html', context={})

def login(request):
    return render(request, 'Genre/login.html')