from django.db import models

class Card(models.Model):
    CARDS = ["green", "purple", "yellow", "white", "red", "blue"]
    colour = models.CharField(max_length = 100, choices = CARDS, null = True, blank = True, default = "blue")
    amount = models.IntegerField(default = 0, editable = False)