# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to generate a list of user to licenses using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_users = json.loads(request.text)

i = 0
while i < len(json_users['items']):
    try:
        request_user_licenses = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users/' + json_users['items'][i]['configurationId']['id'] + '?select=licenseProperties.licenseActive,licenseProperties.additionalLicenses,licenseProperties.hasClientAccess,licenseProperties.mediaLevel', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
        json_user_licenses = json.loads(request_user_licenses.text)
        
        licenses = ''
        ii = 0
        try:
            while ii < len(json_user_licenses['licenseProperties']['additionalLicenses']):
                licenses += json_user_licenses['licenseProperties']['additionalLicenses'][ii]['displayName'] + ', '
                ii += 1
        except:
            licenses = 'NA  '
        print(json_users['items'][i]['configurationId']['id'] + ' (License Active: ' + str(json_user_licenses['licenseProperties']['licenseActive']) + '; Client Access: ' + str(json_user_licenses['licenseProperties']['hasClientAccess']) + '; Media Level: ' + str(json_user_licenses['licenseProperties']['mediaLevel']) + '; Additional Licenses: ' + licenses[:-2] + ')')
        i += 1
    except:
        print(json_users['items'][i]['configurationId']['id'] + ' (NA)')
        i += 1
