from django.urls import path
from actions.views import deposite, wire_money, show_balance

urlpatterns = [
    path('deposite/<int:card_id>', deposite),
    path('wire-money/<int:sender_id>/<int:reciever_id>', wire_money),
    path('show_balance/<int:card_id>', show_balance)
]