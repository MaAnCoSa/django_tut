from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(*args, **kargs):
    return HttpResponse("<h1>Hello World</h1>")