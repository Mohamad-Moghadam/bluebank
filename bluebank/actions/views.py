from django.shortcuts import render
from actions.models import Card
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def deposite(request, card_id : int):
    if request.method == 'POST':
        data = json.loads(request.body)
        desired_card = get_object_or_404(Card, id = card_id)
        desired_card.amount += data.get("amount")
        desired_card.save()

        return HttpResponse(f"deposited {data.get('amount')}")

@csrf_exempt
def wire_money(request, sender_id : int, reciever_id : int):
    if request.method == 'POST':
        sender = get_object_or_404(Card, id = sender_id)
        reciever = get_object_or_404(Card, id = reciever_id)

        data = json.loads(request.body)

        if sender.amount < data.get("amount"):

            sender.amount -= data.get("amount")
            reciever.amount += data.get("amount")

            sender.save()
            reciever.save()

            return HttpResponse(f"transaction completed.")
        
        else:
            return HttpResponse(f"transaction failed. not enough money. ")

def show_balance(request, card_id : int):
    desired_card = get_object_or_404(Card, id= card_id)
    return HttpResponse(f"you currently have {desired_card.amount}")
