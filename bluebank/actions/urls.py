from django.urls import path
from actions.views import deposite, wire_money, show_balance, get_loan, pay_installation

urlpatterns = [
    path('deposite/<int:card_id>', deposite),
    path('wire-money/<int:sender_id>/<int:reciever_id>', wire_money),
    path('show_balance/<int:card_id>', show_balance),
    path('get-loan/<int:card_id>', get_loan),
    path('pay-installation/<int:loan_id>/<int:card_id>', pay_installation)
]