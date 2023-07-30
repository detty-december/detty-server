import json

from django.http import JsonResponse
from django.views import View

from api.v1.models import User


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


class BusinessEventView(View):
    def get(self, request, *args, **kwargs):
        owner_id = request.GET.get('ownerid')
        data = {
            'message': 'Events owned by the specified owner',
            'version': 'v1',
        }

        return JsonResponse(data)


class BusinessUserView(View):
    def post(self, request, *args, **kwargs):
        print(request)
        data = json.loads(request.body)
        print(data)
        user_id = data.get('userId')
        new_user = User.objects.create(user_id=user_id, user_type=1)  # Set user_type as needed
        response_data = {
            'message': 'User created successfully',
            'version': 'v1',
            'user_id': str(new_user.user_id),
        }

        return JsonResponse(response_data, status=201)
