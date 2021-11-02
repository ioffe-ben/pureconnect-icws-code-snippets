# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to connect to PureConnect Premise environment using ICWS API.
import json
import requests

# Disable warning for self-signed SSL certificates
requests.packages.urllib3.disable_warnings()

# Connection variables
server = '<ic_server>'
protocol = "http" # http or https
port = "8018" # 8018 or 8019
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
baseURL = f"{protocol}://{server}:{port}/icws/"

# Connection request
request = requests.post(baseURL + 'connection', headers=header, data=json.dumps(body), verify=False)

if 'csrfToken' in request.text:
    json_connection_response = json.loads(request.text)
    print('----ICWS SESSION INITIATED----\nCSRF Token: ' + json_connection_response['csrfToken'] + '\nSession ID: ' + json_connection_response['sessionId'] + '\n' + '-' * 30)
else:
    print('Connection error: ' + request.text)
    raise ConnectionError('An error has occurred')

header['ININ-ICWS-CSRF-Token'] = json_connection_response['csrfToken']
cookie = request.cookies
