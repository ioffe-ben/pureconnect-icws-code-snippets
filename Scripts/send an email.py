# Copyright (c) 2021, Ben Ioffe (https://github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
import json
import requests

# Disable warning for self-signed SSL certificates
requests.packages.urllib3.disable_warnings()

# region ICWS connection
# region PureConnect Cloud enviroment
servers_file = requests.get('<>')
j_servers_file = json.loads(servers_file.text)
server = j_servers_file['servers'][0]['altHostHints']
# endregion

# region Connection variables
baseURL = j_servers_file['serviceUrlTemplate'].replace("{host}/", server[0]) + "/icws/"
userID = '<>'
password = '<>'
applicationName = '<>'
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
    print('----ICWS SESSION INITIATED----\nCSRF Token: ' + jreq['csrfToken'] + '\nSession ID: ' + jreq['sessionId'] + '\n' + '-' * 30)
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

body = {'recipients': ["benyamin.ioffe@gmail.com"],
        'subject': 'Python Test Email',
        'body': 'This is a test message!'}

req = requests.post(baseURL + jreq['sessionId'] + '/configuration/mail/send-email', headers=header, cookies=cookie, data=json.dumps(body), verify=False)

if req.status_code == 204:
    print('Response Header: ' + str(req.status_code) + ' as expected, email sent successfully!')
else:
    print('Response Header: ' + str(req.status_code))
    print('Error: ' + req.headers)
# endregion
