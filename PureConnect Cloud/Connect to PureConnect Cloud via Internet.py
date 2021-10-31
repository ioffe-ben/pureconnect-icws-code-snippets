# Copyright (c) 2021, Ben Ioffe (https://github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
import json
import requests

# Disable warning for self-signed SSL certificates
requests.packages.urllib3.disable_warnings()

# region ICWS connection
# region PureConnect Cloud enviroment
servers_file = requests.get('https://apps.caas.com/<friendlyname>/customICWS/config/servers.json')
j_servers_file = json.loads(servers_file.text)
server = j_servers_file['servers'][0]['altHostHints']
# endregion

# region Connection variables
baseURL = j_servers_file['serviceUrlTemplate'].replace("{host}/", server[0]) + "/icws/"
userID = '<ic username>'
password = '<ic password>'
applicationName = '<application name>'
language = "en-us"
# endregion

# region Connection Body and Header
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName': applicationName,
        'userID': userID,
        'password': password}
header = {'Accept-Language': language}
# endregion

# region Connection request
req = requests.post(baseURL + 'connection', headers=header, data=json.dumps(body), verify=False)

if 'csrfToken' in req.text:
    jreq = json.loads(req.text)
    print('ICWS SESSION INITIATED!\n' + '-' * 30 + '\nCSRF Token: ' + jreq['csrfToken'] + '\nSession ID: ' + jreq['sessionId'] + '\n' + '-' * 30)
else:
    print('Error: ' + req.text)
    raise ConnectionError('An error has occurred')

header['ININ-ICWS-CSRF-Token'] = jreq['csrfToken']
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName': applicationName,
        'sessionId': jreq['sessionId']}
cookie = req.cookies
# endregion
# endregion

# region Main code
# Get all workgroups
req = requests.get(baseURL + jreq['sessionId'] + '/configuration/workgroups', headers=header, cookies=cookie, data=json.dumps(body), verify=False)

rolereq = json.loads(req.text)

i = 0
while i < len(rolereq['items']):
  print(rolereq['items'][i]['configurationId']['id'])
  i += 1
# endregion
