import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from detty_server.models import User


@require_http_methods(['POST'])
def get_events(request):
    videos = User.objects.all()
    data = [video.to_dict() for video in videos]
    return JsonResponse({'data': data})


@require_http_methods(['GET'])
def video_detail(request, pk):
    video = User.objects.get(pk=pk)
    data = video.to_dict()
    return JsonResponse({'data': data})