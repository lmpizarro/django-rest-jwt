import requests
import time
import json

be_url = "http://localhost:8080/{}"
header = {'Content-type': 'application/json'}


def set_header(authorization):
    header['Authorization'] = f'Bearer {authorization}'


# curl http://127.0.0.1:8080/api/token/ -d "username=admin&password=admin"
def login(user='admin', password='admin'):
    import requests

    url = be_url.format('api/token/')

    payload = {'username': user, 'password': password}
    headers= {}

    response = requests.post(url, headers=headers, data = payload)

    return response.json()


if __name__ == '__main__':
    credentials = login()
    
    print(credentials)
