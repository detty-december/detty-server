import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from detty_server.models import User


def home(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data, safe=False)
