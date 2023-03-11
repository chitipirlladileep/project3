from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def app_first(request):
    return HttpResponse('This is my first view')
