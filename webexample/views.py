from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    x=5
    y=8
    z=x+y
    return HttpResponse(z)


def about(request):
    return HttpResponse("<h3>hello about!</h3>")