from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, "henry.html")


def greet(request):
    return HttpResponse("Welcome to django project")
