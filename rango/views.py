from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!<br><a href='about/'>About</a>")

def views(request):
    return HttpResponse("Hello views")

def about(request):
    return  HttpResponse("Rango says here is the about page")