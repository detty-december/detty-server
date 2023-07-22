from django.views import View
from django.http import JsonResponse


class EventView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'message': 'This is version 1 of my endpoint.',
            'version': 'v1',
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        print(request.body)
        return JsonResponse({'message': 'hi',
                             'version': 'v1'})
