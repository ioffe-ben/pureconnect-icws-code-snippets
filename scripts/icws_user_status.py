# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to set and retrieve IC user status using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

ic_username = '<ic_username>'

# Retrieves the IC user status
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/status/user-statuses/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
get_status_message = json.loads(request.text)
print(ic_username + ' IC status is ' + get_status_message['statusId'])
print(get_status_message)

# Updates the  IC user status
body = {"statusId" : "On Vacation"}
request = requests.put(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/status/user-statuses/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)
get_status_message = json.loads(request.text)
if request.status_code == 202:
    print('IC status updated successfully!')
else:
    print('Error: ' + get_status_message)

# Retrieving a list of all IC users statuses
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_users = json.loads(request.text)

i = 0
while i < len(json_users['items']):
    request_user_statuses = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users/' + json_users['items'][i]['configurationId']['id'] + '?select=statusText', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
    json_user_statuses = json.loads(request_user_statuses.text)
    print(json_users['items'][i]['configurationId']['id'] + ' (' + json_user_statuses['statusText'] + ')')
    i += 1
