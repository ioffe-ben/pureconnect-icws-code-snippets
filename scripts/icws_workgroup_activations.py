# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to set and get the workgroup activations for a single user using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Get the current workgroup activations for a single user
ic_username = '<ic_username>'
request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/activations/users/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_response = json.loads(request.text)
print(json_response)

# Sets current workgroup activations for a single user
body = {"activations":{"<workgroup_name>":False}}
request = requests.put(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/activations/users/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, data=json.dumps(body), verify=False)
json_response = json.loads(request.text)
print(json_response)
