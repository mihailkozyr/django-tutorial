from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("We're the champions, my friend!")
# Create your views here.
