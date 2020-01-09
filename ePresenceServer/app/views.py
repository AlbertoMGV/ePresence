from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import (HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_200_OK)
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from app.models import Aula
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.

def login(request):
    return render(request, 'login.html')

def home(request):
	aulas = Aula.objects.all()
	return render(request, 'home.html', {'aulas': aulas})

def aula(request, id):
	aula = Aula.objects.get(id=id)
	return render(request, 'aula.html', {'aula': aula})

def aula_p_add(request, id):
	aula = Aula.objects.get(id=id)
	aula.personas = aula.personas+1
	aula.save()
	return HttpResponse('ok')

def aula_p_remove(request, id):
	aula = Aula.objects.get(id=id)
	aula.personas = aula.personas-1
	aula.save()
	return HttpResponse('ok')

def aula_e_verde(request, id):
	aula = Aula.objects.get(id=id)
	aula.estado = 0
	aula.save()
	return HttpResponse('ok')

def aula_e_rojo(request, id):
	aula = Aula.objects.get(id=id)
	aula.estado = 2
	aula.save()
	return HttpResponse('ok')

def aula_e_amarillo(request, id):
	aula = Aula.objects.get(id=id)
	aula.estado = 1
	aula.save()
	return HttpResponse('ok')
