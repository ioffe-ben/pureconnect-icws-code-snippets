# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to connect to PureConnect Cloud enviroment using ICWS API. 
import json
import requests

# Disable warning for self-signed SSL certificates
requests.packages.urllib3.disable_warnings()

# Get servers.json file to retrive PureConnect Cloud enviroment base URL. Mmore info about this - https://help.genesys.com/developer/cic/docs/icws/webhelp/ConceptualContent/GettingStarted_Connecting.htm
servers_file = requests.get('https://apps.caas.com/<friendlyname>/customICWS/config/servers.json')
json_servers_file = json.loads(servers_file.text)
server = json_servers_file['servers'][0]['altHostHints']

# Connection variables
baseURL = json_servers_file['serviceUrlTemplate'].replace("{host}/", server[0]) + "/icws/"
userID = '<ic_username>'
password = '<ic_password>'
applicationName = '<ic_application_name>'
language = "en-us"

# Connection Body and Header
body = {'__type': 'urn:inin.com:connection:icAuthConnectionRequestSettings',
        'applicationName': applicationName,
        'userID': userID,
        'password': password}
header = {'Accept-Language': language}

# Connection request
request = requests.post(baseURL + 'connection', headers=header, data=json.dumps(body), verify=False)

if 'csrfToken' in request.text:
    json_connection_response = json.loads(request.text)
    print('ICWS SESSION INITIATED!\n' + '-' * 30 + '\nCSRF Token: ' + json_connection_response['csrfToken'] + '\nSession ID: ' + json_connection_response['sessionId'] + '\n' + '-' * 30)
else:
    print('Connection error: ' + request.text)
    raise ConnectionError('An error has occurred')

header['ININ-ICWS-CSRF-Token'] = json_connection_response['csrfToken']
cookie = request.cookies
