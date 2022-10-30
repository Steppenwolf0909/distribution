from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests

hosts=['1', '2', '3', '4', '5']
last_host=-1

@api_view(('GET',))
def send_to(request):
    req = 'No any alive servers ;('
    for host in hosts:
        try:
            URL = get_url()
            req = requests.get(URL)
            return Response(req)
            break
        except:
            pass
    return Response(req)


def get_url():
    global last_host
    last_host += 1
    print(int(hosts[len(hosts)-1]))
    if (last_host == 5):
        last_host = 0
    URL = f"http://node{hosts[last_host]}:800{hosts[last_host]}/service"
    return URL