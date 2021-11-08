# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to send an email using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Set the Interaction ID
interaction_id = '<interaction_id>'

# Places the interaction on hold
body = {'on': True} # to take it off hold, change to be: body = {'on': False}
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/hold', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Places the interaction on mute
body = {'on': True} # to change the state: body = {'on': False}
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/mute', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Places the interaction on pause
body = {'on': True} # to change the state: body = {'on': False}
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/pause', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Changes the record state of the interaction
body = {
        'on': True,
        'supervisor': False
        }
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/record', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Sends an interaction to voicemail
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/send-to-voicemail', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Sends DTMF digits to an interaction
body = {'dtmfDigits': '1'}
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/send-digits', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': error')
    
# Performs a pickup on the interaction
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/pickup', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')

# Disconnects the interaction
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id + '/disconnect', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the action was successfully performed')
else:
    print(str(request.status_code) + ': Error')
