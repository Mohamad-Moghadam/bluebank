from django.db import models
from user.models import User

class Card(models.Model):
    CARDS = [("green", "Green"), ("purple", "Purple"), ("yellow", "Yellow"), ("white", "White"), ("red", "Red"), ("blue", "Blue")]
    colour = models.CharField(max_length = 100, choices = CARDS, null = True, blank = True, default = "blue")
    amount = models.IntegerField(default = 0, editable = False)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="cards_of_the_user"  # Ensure this matches in queries
    )