import uuid

from django.shortcuts import render

from detty_server.models import User


def home(request):
    User.objects.create(user_id=uuid.uuid4())
    return render(request, "home.html")
