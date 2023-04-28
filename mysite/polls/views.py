from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
#from django.template import loader

# Create your views here.
def index(request):
    question_list = Question.objects.order_by("-pub_date")[:5]
    
    #template = loader.get_template('polls/index.html')
    context = {
        "question_list": question_list,
    }
    return render(request, "polls/index.html", context)
    #return HttpResponse(template.render(context, request))



def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
        
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")
    return render(request, 'polls/details.html',{"question" : question})
    
    #return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)