from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

counter=0

@api_view(('GET',))
def service(request):
    global counter
    counter+=1
    print(f'Server{request.META["SERVER_PORT"]} work on {counter}"s request')
    return Response(f'Server{request.META["SERVER_PORT"]} work on {counter}"s request', status=status.HTTP_200_OK)
