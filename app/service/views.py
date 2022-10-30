from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import time

from . import models

counter=0

@api_view(('GET',))
def service(request):
    global counter
    counter+=1
    print(models.RequestCounter.objects.all())
    models.RequestCounter.objects.update_or_create(
        server_port=int(request.META["SERVER_PORT"]),
        defaults={
            "count": counter,
        }
    )
    return Response(f'Server {request.META["SERVER_PORT"]} made {counter} requests', status=status.HTTP_200_OK)

