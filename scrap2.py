import requests
token = ""
api_url = ""
url = "{}?access_token={}".format(api_url,token)
req_json = requests.get(url).json()
print(req_json)
for repo in req_json:
    print(repo)
    
