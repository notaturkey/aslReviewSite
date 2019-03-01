from django.shortcuts import render

# Create your views here.
import random

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import word2

def index(request):
    template = loader.get_template('unit2/index.html')
    latest_word_list = word2.objects.all()
    context = {'latest_word_list': latest_word_list, 'rando_num': random.randint(1,117)}
    return HttpResponse(template.render(context, request))
    
def detail(request, random_wor):
    template = loader.get_template('unit2/detail.html')
    wordet = word2.objects.get(pk = random_wor) 
    latest_word_list = word2.objects.all()
    prev= 244 if(random_wor - 1 < 1) else random_wor - 1
    next= 1 if(random_wor + 1 > 244) else random_wor + 1
    context = {'latest_word_list': latest_word_list,'random_word': wordet.random_word,'rando_num': random.randint(1,117), 'url': wordet.url.replace(" ", "+"), id: random_wor,'prev': prev, 'nxt':next}  
    return HttpResponse(template.render(context, request))