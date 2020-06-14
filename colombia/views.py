from django.http import HttpResponse
import json

def list_cities(request):

    data = {
        'status': 'ok',
        'country': 'Colombia',
        'top_ten': [
            'bogota',
            'cali',
            'medellin',
            'cartagena',
        ],
        'message': 'Colombia tierra linda'
    }
    return HttpResponse(json.dumps(data))

def view_city(request, city):
    data = {
        'status': 'ok',
        'country': city,
        'population': 1247841,
        'cases': 1264,
        'recovered': 952,
        'death': 52,
        'UCI':67
    }
    return HttpResponse(json.dumps(data))