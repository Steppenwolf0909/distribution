from email.policy import default
from django.db import models


class RequestCount(models.Model):
    server_port = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


    def __str__(self):
        return self.emserver_port
