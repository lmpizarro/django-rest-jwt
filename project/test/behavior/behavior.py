import requests
import json

import utils as utils

def hello():
    utils.login()
    url_hello = utils.be_url.format("api/hello/")

    response = requests.get(url_hello, headers=utils.header)

    return response.json()

def create(user='lmpizarro', password='pepe', email='pepe@pepe.com'):
    url = utils.be_url.format('account/create/')

    payload = {'username': user, 'password': password, 'email': email}
    headers = {}

    response = requests.post(url, headers=headers, data=payload)

    return response.json()

if __name__ == '__main__':

    utils.print_out(hello(), 'checkin')
    utils.print_out(create(), 'create')

