"""mercanotas_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.http import HttpResponse

import json

from colombia import views as colombia_views

def hola(request):
    return HttpResponse('Hola Beto como vas? \n si te llego el correo?')

def prueba1(request):
    return HttpResponse('la otra url Si corre Juy !!!!!!!!!!!!!!!!!!!! :D')

def prueba2(request):
    data = {
        'status': 'ok',
        'country': request.GET['country'],
        'message': 'Tu pais es muy bonito'
    }
    print(request.GET['country'])
    return HttpResponse(json.dumps(data), content_type='application/json')
    
def prueba3(request, country):
    data = {
        'status': 'ok',
        'country': country,
        'message': 'Tu pais es muy bonito'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def prueba4(request, country, depart):
    data = {
        'status': 'ok',
        'country': country,
        'depart': depart,
        'message': 'Tu pais es muy bonito'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

urlpatterns = [
    path('', hola),
    path('prueba1/', prueba1),
    path('pais/', prueba2),
    path('pais/<str:country>', prueba3),
    path('pais/<str:country>/<str:depart>', prueba4),

    path('colombia/', colombia_views.list_cities),
    path('colombia/<str:city>', colombia_views.view_city),
]
