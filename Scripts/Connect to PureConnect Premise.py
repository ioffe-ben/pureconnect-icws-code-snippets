# Copyright (c) 2021, Ben Ioffe (https://github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.

import csv
import json
import requests
 
# disable warning for self signed SSL cert
requests.packages.urllib3.disable_warnings()
 
# required vars
user = '<ic username>'
passw = '<ic password>'
server = '<ic server>'
applicationName = '<application name>'
lang = "en-us"
protocol = "http" #http or https
port = "8018" #8018 or 8019
 

# Connection Request body, header and base URL
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName' : applicationName,
        'userID' : user,
        'password' : passw }
header = {'Accept-Language': lang }
url = f"{protocol}://{server}:{port}/icws/"
print(url)

req = requests.post(url + 'connection', headers=header, data=json.dumps(body), verify=False)
 
if 'csrfToken' in req.text:
    jreq = json.loads(req.text)
else:
    raise ConnectionError('An error has occurred')
    
header['ININ-ICWS-CSRF-Token'] = jreq['csrfToken']
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName': applicationName,
        'sessionId': jreq['sessionId']}
cookie = req.cookies

req = requests.get(url + jreq['sessionId'] + '/configuration/workgroups', headers=header, cookies=cookie, data=json.dumps(body), verify=False)

rolereq = json.loads(req.text)

i = 0
while i < len(rolereq['items']):
  print(rolereq['items'][i]['configurationId']['id'])
  i += 1
