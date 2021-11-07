# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to generate a .csv document with IC users, workgroups, roles, skills, wrap-up codes, and wrap-up categories using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Generate a .csv document with IC users
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'IC Usernames\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('ic_users_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "ic_users_export.csv" file in the same folder as this script')

# Generate a .csv document with workgroups
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/workgroups', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'Workgroups\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('workgroups_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "workgroups_export.csv" file in the same folder as this script')

# Generate a .csv document with roles
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/roles', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'Roles\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('roles_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "roles_export.csv" file in the same folder as this script')

# Generate a .csv document with skills
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/skills', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'Skills\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['id']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('skills_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "skills_export.csv" file in the same folder as this script')

# Generate a .csv document with Wrap-up Codes
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/wrap-up-codes', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'Wrap-up Codes\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['displayName']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('wrap-up-codes_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "wrap-up-codes_export.csv" file in the same folder as this script')

# Generate a .csv document with Wrap-up Categories
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/wrap-up-categories', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_items = json.loads(request.text)

i = 0
csv_export_string = 'Wrap-up Codes\n'

while i < len(json_items['items']):
    item = json_items['items'][i]['configurationId']['displayName']
    i += 1
    csv_export_string = csv_export_string + item + '\n'
    print('(' + str(i) + ' out of ' + str(len(json_items['items'])) + ') ' + item)

with open('wrap-up-categories_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "wrap-up-categories_export.csv" file in the same folder as this script')
