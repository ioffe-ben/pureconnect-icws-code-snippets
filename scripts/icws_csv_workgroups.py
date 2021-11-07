# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to generate a .csv document with workgroups using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/workgroups', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_workgroups = json.loads(request.text)

i = 0
csv_export_string = 'Workgroups\n'

while i < len(json_workgroups['items']):
    request_workgroup = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/workgroups/' + json_workgroups['items'][i]['configurationId']['id'],headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
    workgroup = json_workgroups['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + workgroup + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_workgroups['items'])) + ') ' + workgroup)

with open('workgroups_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "workgroups_export.csv" file in the same folder as this script')
