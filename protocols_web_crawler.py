import requests
import json
import sys


# variables
url = 'https://files.support.sandvine.com/'
username = sys.argv[1]
password = sys.argv[2]
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
        print('key is : {}'.format(key))
        # Item on the other hand is multiple objects in string so lets iterate:
        for i in range(0, len(item)):
            r_object = item[i]
            print(str(i) + ' : ' + r_object['name'])


# Work on grabbing token by authing
response = requests.post(url='https://files.support.sandvine.com/accounts/login', headers=headers, data=json.dumps(payload), auth=(username,password))

print("--------------------------")
# ## This works: commenting Quick get request and print families
family_request = requests.get(url='https://files.support.sandvine.com/software/families', headers=headers, auth=(username,password))
print('Families Directories: ')
print("--------------------------")
# print using function
printAllOptions(request_string=family_request)

print("--------------------------")

# Next tree : Protocols directories
request_2 = requests.get(url='https://files.support.sandvine.com/software/family/Protocols/product/Protocols/streams', headers=headers, auth=(username,password))
print('Stream Directories: ')
# print using function
#printAllOptions(request_string=request_2)

print("--------------------------")

return_object = request_2.json()

def returnList():
    for key,item in return_object.items():
        # for i in range(0, len(item)):
        #     print(item[i]['name'])
        # print(item)
        # print(type(item))
        return [x['name'] for x in item]

for x in returnList()[:-4:-1]:
    r = requests.get(url='https://files.support.sandvine.com/software/family/Protocols/product/Protocols/stream/' + x + '/release/', headers=headers, auth=(username, password))
    print(r.text)





# Ok lets grab files from release
# request_4 = requests.get(url='https://files.support.sandvine.com/software/family/Protocols/product/Protocols/stream/18.04/release/18.04.01', headers=headers, auth=(username,password))
# print('Download Directories: ')
# # cant use same print function
# request_4_object = request_4.json()
# request_4_object_documents = request_4_object['documents']
# request_4_object_downloads = request_4_object['downloads']
# request_4_object_release = request_4_object['release']
