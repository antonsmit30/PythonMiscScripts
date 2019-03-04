## Script to return latest LTIP package download.
## Requests Requests package

import requests
import json
import sys

# variables
url = 'https://files.support.sandvine.com/'

username = sys.argv[1]
password = sys.argv[2]

centos_version = 7

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'files.support.sandvine.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

payload = {
    'email': username,
    'password': password
}


def printAllOptions(request_string):
    return_object = request_string.json()
    for key,item in return_object.items():
        # Our key is only 1 item great
        # Item on the other hand is multiple objects in string so lets iterate:
        for i in range(0, len(item)):
            r_object = item[i]


def return_last_outputs(request_string):
    return_object = request_string.json()
    for key,item in return_object.items():
        if(item):
            # Item on the other hand is multiple objects in string so lets iterate:
            return item[-1]['name'], item[-2]['name'], item[-3]['name']

def return_last_output(request_string):
    return_object = request_string.json()
    for key,item in return_object.items():
        if item:
            # Item on the other hand is multiple objects in string so lets iterate:
            print(item[-1]['name'])
            return item[-1]['name']


def last_protocol_pack_url(last_pack):
    # release_dir,
    for i in last_pack:
        my_local_url = 'https://files.support.sandvine.com/software/family/Protocols/product/Protocols/stream/' \
              + i + '/releases'

        r = requests.get(
            url=my_local_url,
            headers=headers, auth=(username, password))
        # ignore empty return object
        if r.json():
            last_output = return_last_output(r)
            return i, last_output

def get_auth_token():
    # Work on grabbing token by authing
    response = requests.post(url='https://files.support.sandvine.com/accounts/login', headers=headers,
                             data=json.dumps(payload), auth=(username, password))
    return response.json()['token']

def main():

    # Staqe 1 : Auth token
    my_token = get_auth_token()

    # Stage 2: Last protocol packs
    result = requests.get(url='https://files.support.sandvine.com/software/family/Protocols/product/Protocols/streams',
                          headers=headers, auth=(username, password))

    # printAllOptions(request_string=result)
    last_protocol_packs = return_last_outputs(result)

    version, release = last_protocol_pack_url(last_protocol_packs)

    # Once we know the version we can print and return the URL to download the file
    my_request = "https://files.support.sandvine.com/" \
                 "software/Protocols/Protocols/" \
                 "{}/{}/Protocols_{}.tar?token={}".format(version, release, release, my_token)
    print("url to download latest LTIP (Please click on link to download: {}".format(my_request))
    return my_request

if __name__ == "__main__":
    main()
