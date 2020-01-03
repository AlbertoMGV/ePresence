from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import (HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND, HTTP_200_OK)
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from app.models import *
from django.core import serializers
from app.serializers import * 
import json

# Create your views here.

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

@api_view(["POST"])
def getAula(request):
	if request.method == 'POST':
		uid = request.data.get('aula_id')
		try:
			res = Aula.objects.all()
			res_ser = AulaSerializer(res, many=True)
			aaa = json.loads(res_ser.data)
			return Response({"result":"ok"}, status=HTTP_200_OK)
		except:
			return Response({'result': "not ok"}, status=HTTP_401_UNAUTHORIZED)