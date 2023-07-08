#...
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):
    template_name = "home.html"
    
class About(View):
    template_name = "about.html"
    