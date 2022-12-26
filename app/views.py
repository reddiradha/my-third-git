from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def radha(request):
    return HttpResponse('This is first function in first app')
def ramya(request):
    return HttpResponse('<h1>this is my second function in first app</h1>')

