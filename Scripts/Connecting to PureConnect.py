import csv
import json
import requests
 
# disable warning for self signed SSL cert
requests.packages.urllib3.disable_warnings()
 
# required vars
user = '<>'
passw = '<>'
server = '<>'
appname = '<>'
lang = "en-us"
 

# Connection Request body, header and base URL
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName' : appname,
        'userID' : user,
        'password' : passw }
header = {'Accept-Language': lang }
url = f"http://{server}:8018/icws/"
print(url)

req = requests.post(url + 'connection', headers=header, data=json.dumps(body), verify=False)
 
if 'csrfToken' in req.text:
    jreq = json.loads(req.text)
else:
    raise ConnectionError('An error has occurred')
