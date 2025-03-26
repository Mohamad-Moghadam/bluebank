from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from user.models import User
import json

@csrf_exempt
def sign_up(request):
    data = json.loads(request.body)
    
    User.objects.create(
        name = data.get("name"),
        last_name = data.get("last_name"),
        user_name = data.get("user_name"),
        cards = data.get("cards"),
    )

