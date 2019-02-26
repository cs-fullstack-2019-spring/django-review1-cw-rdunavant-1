from django.http import HttpResponse
from .models import Page
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hey!")