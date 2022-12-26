from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def lavanya(request):
    return HttpResponse('<marquee>this is my first function in second app<marquee>')
def sukanya(request):
    return HttpResponse('<b>this is my second function in second app</b>')
