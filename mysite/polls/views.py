from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the pools index.")

def hello(request):                          
    return HttpResponse("Hello, world!")     


def medved(request):
    try:
        with open("c:\\kozyr\\django\\mysite\\polls\\static\\Preved.jpg", "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
    
    return HttpResponse("Hello, world!")