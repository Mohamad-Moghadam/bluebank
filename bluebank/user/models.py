from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)