from django.db import models
from user.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Card(models.Model):
    CARDS = [("green", "Green"), ("purple", "Purple"), ("yellow", "Yellow"), ("white", "White"), ("red", "Red"), ("blue", "Blue")]
    colour = models.CharField(max_length = 100, choices = CARDS, null = True, blank = True, default = "blue")
    amount = models.BigIntegerField(default = 0, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards_of_the_user")
    number = PhoneNumberField(region = "IR")


class Loan(models.Model):
    card = models.ForeignKey(Card, on_delete= models.CASCADE, related_name= "loans_of_each_card")
    amount = models.BigIntegerField()
    number_of_installation = models.IntegerField()