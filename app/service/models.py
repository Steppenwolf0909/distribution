from email.policy import default
from django.db import models

class RequestCounter(models.Model):
    server_port = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
