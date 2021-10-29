from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, View
import requests
from django.http import FileResponse, Http404
import json
from django.http import HttpResponse, JsonResponse
import io


# Create your views here.

def data1(request):
    url = "http://localhost:8000/reportes/"
    #url = "http://jacgsaw.com/siath/app/war"
    datos =     {"url": "popeye@yahoo.com.co","username": "popeye", "email": "popeye@yahoo.com.co", "is_staff": "S"}
    respuesta = requests.get(url, data=datos)

    if respuesta.status_code == 200:
        print("Esto recibo del REST")
        print (respuesta.status_code)
        buffer = io.BytesIO()
        buffer.write(respuesta.content)

        buffer.close()
        return FileResponse(respuesta, filename='somename.pdf' , content_type='application/pdf')

    context = {}
  
    return render(request, 'inicio4.html', context)




