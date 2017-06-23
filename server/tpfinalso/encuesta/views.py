from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from encuesta.models import Question
import json
# Create your views here.

def index(request):
    return HttpResponse("Guada re crack, el año que viene va a tener BD 1 con Vale <3")

def preguntaID(request,preg):
    try:
        q = serializers.serialize("json",[Question.objects.get(pk=preg)])
    except Question.DoesNotExist:
        q= "no existe"
    return HttpResponse(q)

def preguntaAll(request):
    q = serializers.serialize("json",Question.objects.all())
    r = [j for j in json.loads(q)]
    t = '<p/>'.join(str(a) for a in r)
    
    return HttpResponse(t)

