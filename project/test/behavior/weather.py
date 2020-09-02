import requests
import json

import utils as utils

def hello():
    utils.login()
    url_hello = utils.be_url.format("api/hello/")

    response = requests.get(url_hello, headers=utils.header)

    return response.json()



if __name__ == '__main__':

    utils.print_out(hello(), 'checkin')
 
