# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how to start, stop, pause, resume screen recordings using ICWS API.
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

# Set the Interaction ID
ic_username = '<ic_username>'

# Start recording the screen of the specified user
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/screenrecordings/record/start/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 202:
    print(str(request.status_code) + ': the start screen recording request was accepted for processing')
else:
    print(str(request.status_code) + ': error')

# Stop all recording the screen of the specified user
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/screenrecordings/record/stop/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 202:
    print(str(request.status_code) + ': the stop screen recording request was accepted for processing')
else:
    print(str(request.status_code) + ': error')

# Pauses all recording the screen of the specified user
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/screenrecordings/record/pause/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 202:
    print(str(request.status_code) + ': the pause screen recording request was accepted for processing')
else:
    print(str(request.status_code) + ': error')

# Resumes all recording the screen of the specified user
request = requests.post(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/screenrecordings/record/resume/' + ic_username, headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)

if request.status_code == 202:
    print(str(request.status_code) + ': the resume screen recording request was accepted for processing')
else:
    print(str(request.status_code) + ': error')
