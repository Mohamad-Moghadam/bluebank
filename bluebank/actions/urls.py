from django.urls import path
from actions.views import deposite, wire_money

urlpatterns = [
    path('deposite', deposite),
    path('wire-money', wire_money),
]
