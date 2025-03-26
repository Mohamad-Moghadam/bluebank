from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from user.models import User
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
    
        User.objects.create(
        name = data.get("name"),
        last_name = data.get("last_name"),
        user_name = data.get("user_name"),
        cards_id = data.get("cards"),
    )

        return HttpResponse(f"{data.get('name')} is now a member.")

def show_profile(request, user_id : int):
    user = get_object_or_404(User, id = user_id)

    return render(request, 'user/show_profile.html', user)

