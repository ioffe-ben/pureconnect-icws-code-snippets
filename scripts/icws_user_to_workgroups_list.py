# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to generate a list of user to workgroups using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_users = json.loads(request.text)

i = 0
while i < len(json_users['items']):
    try:
        request_user_workgroups = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users/' + json_users['items'][i]['configurationId']['id'] + '?select=workgroups', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
        json_user_workgroups = json.loads(request_user_workgroups.text)

        members = ''
        ii = 0
        while ii < len(json_user_workgroups['workgroups']):
            members += json_user_workgroups['workgroups'][ii]['id'] + ', '
            ii += 1
        print(json_users['items'][i]['configurationId']['id'] + ' (' + members[:-2] + ')')
        i += 1
    except:
        print(json_users['items'][i]['configurationId']['id'] + ' (NA)')
        i += 1
