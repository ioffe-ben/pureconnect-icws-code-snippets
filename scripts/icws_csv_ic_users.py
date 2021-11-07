# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to generate a .csv document with IC users using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_users = json.loads(request.text)

i = 0
csv_export_string = 'IC Usernames\n'

while i < len(json_users['items']):
    request_user_data_all = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users/' + json_users['items'][i]['configurationId']['id'],headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
    json_user_data = json.loads(request_user_data_all.text)
    ic_username = json_users['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + ic_username + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_users['items'])) + ') ' + ic_username)

with open('ic_users_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "ic_users_export.csv" file in the same folder as this script')
