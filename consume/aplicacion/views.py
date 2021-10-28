from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, View
import requests
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.

def data1(request):
    url = "http://localhost:8000/usuario/usuario/"
    #url = "http://jacgsaw.com/siath/app/war"
    datos =     {"url": "popeye@yahoo.com.co","username": "popeye", "email": "popeye@yahoo.com.co", "is_staff": "S"}
    response = requests.post(url, data=datos)

    if response.status_code == 200:
        print(response.text)
        resultado0 = response.text
        

    context = {}
    # Pruebas
    
    return render(request, 'inicio4.html', context)



