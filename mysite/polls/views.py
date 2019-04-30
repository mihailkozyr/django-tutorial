from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the pools index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)


def hello(request):                          
    return HttpResponse("Hello, world!")     

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

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