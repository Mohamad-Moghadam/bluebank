from django.urls import path
from actions.views import deposite, wire_money

urlpatterns = [
    path('deposite/<int:card_id>', deposite),
    path('wire-money/<int:sender_id>/<int:reciever_id>', wire_money),
]