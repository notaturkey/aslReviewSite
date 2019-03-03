from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import word

def index(request):
    template = loader.get_template('polls/index.html')
    latest_word_list = word.objects.all()
    context = {'latest_word_list': latest_word_list, 'rando_num': random.randint(1,332)}
    return HttpResponse(template.render(context, request))
    
def detail(request, random_wor):
    template = loader.get_template('polls/detail.html')
    wordet = word.objects.get(pk = random_wor) 
    latest_word_list = word.objects.all()
    prev= 332 if(random_wor - 1 < 1) else random_wor - 1
    next= 1 if(random_wor + 1 > 332) else random_wor + 1
    context = {'latest_word_list': latest_word_list,'random_word': wordet.random_word,'rando_num': random.randint(1,332), 'url': wordet.url.replace(" ", "+"), id: random_wor,'prev': prev, 'nxt':next}  
    return HttpResponse(template.render(context, request))
    