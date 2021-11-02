# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to send an email using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

body = {'recipients': ["email-address@domain.com"],
        'subject': 'Python Test Email',
        'body': 'This is a test message!'}

request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/mail/send-email', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 204:
    print('Response Header: ' + str(request.status_code) + ' as expected, email sent successfully!')
else:
    print('Response Header: ' + str(request.status_code))
    print('Error: ' + request.headers)
