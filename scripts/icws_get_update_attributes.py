# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to get and update the set of attributes from an interaction using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Set the Interaction ID
interaction_id = '<interaction_id>'

# Gets a set of attributes from an interaction
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
request_json = json.loads(request.text)
if request.status_code == 200:
    print(request_json)
else:
    print(str(request.status_code) + ': Error')

# Updates the set of attributes on an interaction
body = {'attributes': {'attr_name1': 'attr_value1', 'attr_name2': 'attr_value2'}}
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/interactions/' + interaction_id, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)

if request.status_code == 200:
    print(str(request.status_code) + ': the attributes were successfully updated')
else:
    print(str(request.status_code) + ': error')
