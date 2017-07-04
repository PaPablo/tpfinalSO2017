from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from encuesta.models import Question,Choice
import json

# Create your views here.

def index(request):
    #return HttpResponse("Guada re crack, el año que viene va a tener BD 1 con Vale <3")
    return HttpResponse("asdas")

def preguntaID(request,preg):
    try:
        q = serializers.serialize("json",[Question.objects.get(pk=preg)])
    except Question.DoesNotExist:
        return HttpResponse("No existe la pregunta")
    return HttpResponse(q, content_type='application/json')

def preguntaAll(request):
    preguntas = serializers.serialize("json", Question.objects.all())

    return HttpResponse(preguntas, content_type='application/json')

def opcionesPorPregunta(request, preg):
    q = serializers.serialize("json", Choice.objects.filter(question=preg))

    return HttpResponse(q, content_type='application/json')

