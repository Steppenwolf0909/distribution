import requests
import time


def main():
    for i in range(100):
        time.sleep(0.5)
        requests.get('http://localhost:8000')


main()

