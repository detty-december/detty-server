from django.views import View
from django.http import JsonResponse


class EventView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'message': 'This is a test get request',
            'version': 'v1',
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {
            'message': 'This is a test post request',
            'version': 'v1',
        }
        return JsonResponse(data)

