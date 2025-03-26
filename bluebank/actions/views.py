from django.shortcuts import render
from actions.models import Card
import json
from django.shortcuts import get_object_or_404

def deposite(request, card_id : int):
    data = json.loads(request.body)
    desired_card = get_object_or_404(Card, card_id)
    desired_card.amount += data.get("amount")
    desired_card.save()

def wire_money(request, sender_id : int, reciever_id : int):
    sender = get_object_or_404(Card, id = sender_id)
    reciever = get_object_or_404(Card, id = reciever_id)

    data = json.loads(request.body)

    if sender.amount < data.get("amount"):

        sender.amount -= data.get("amount")
        reciever.amount += data.get("amount")

        sender.save()
        reciever.save()
