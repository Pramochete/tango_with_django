from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Page

# Create your views here.
def index(request):
    # Query the database for a list of All categories currently stored
    # Order the categories by no. of likes in descending order
    # Retrieve the top 5 only - or all if less than 5
    # Place the list in out context_dict dictionary
    # that will be passed to the template engine

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}

    # Render the response and send it back
    return render(request, 'rango/index.html', context_dict)

def views(request):
    return HttpResponse("Hello views")

def about(request):
    return render(request, 'rango/about.html',{})