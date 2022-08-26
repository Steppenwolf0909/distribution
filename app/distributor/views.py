from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
ports=[8001, 8002, 8003]
last_port=-1
# URL = f"http://localhost:{ports[0]}/service"


@api_view(('GET',))
def send_to(request):
    for port in ports:
        try:
            URL = get_url()
            req = requests.get(URL)
            return Response(req)
            break
        except:
            pass
    return Response(req)


def get_url():
    global last_port
    last_port = last_port + 1
    if (last_port == 3):
        last_port = 0
    URL = f"http://localhost:{ports[last_port]}/service"
    return URL