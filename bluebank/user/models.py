from django.db import models
from actions.models import Card

class User(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)
    cards = models.ForeignKey(to = Card, on_delete = models.PROTECT, related_name = "users_cards", default = 1)