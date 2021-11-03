# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to subscribe, send, and receive a Custom Notification using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Subscribing to Notifications Sent by a Handler
body = {
            "headers": [{
                "objectId": "Test_objectId",
                "eventIds": ["Test_eventId"]
            }]
        }

request = requests.put(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/messaging/subscriptions/system/handler-sent-notifications', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 204:
    print('The subscription to handler-sent notifications has been created!')
else:
    print('Error: Header ' + str(request.status_code))

# Sends a custom notification
body = {
    "objectId": "Test_objectId",
    "eventId": "Test_eventId",
    "data": ["value1", "value2"]
}

request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/system/handler-notification', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 202:
    print('Custom notification sent!')
else:
    print('Error: Header' + request.status_code)

# Receive a Custom Notification
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/messaging/messages', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
response_json = json.loads(request.text)

print(response_json)
